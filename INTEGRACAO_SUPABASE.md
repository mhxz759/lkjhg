# 🚀 Integração Lynx Dev - Next.js + Supabase + Bot Telegram

## 📋 Visão Geral

Este guia descreve como integrar o painel administrativo **Lynx Dev** (Next.js) com o **Supabase** e sincronizar com seu **bot Telegram**.

### Arquitetura

```
Bot Telegram (Python)
    ↓ (insere/atualiza dados)
    ↓
Supabase (banco de dados)
    ↑ (consulta em tempo real)
    ↑
Painel Web Lynx Dev (Next.js)
```

---

## 🔧 Pré-requisitos

1. **Conta Supabase**: [supabase.com](https://supabase.com)
2. **Node.js 18+**: Para rodar o painel web
3. **Python 3.8+**: Para o bot Telegram
4. **Projeto Supabase**: Criado e configurado

---

## 📊 Estrutura do Banco de Dados Supabase

### 1. Tabela `bot_users`

```sql
CREATE TABLE bot_users (
  id SERIAL PRIMARY KEY,
  telegram_id BIGINT UNIQUE NOT NULL,
  username VARCHAR(255),
  name_user VARCHAR(255),
  balance NUMERIC DEFAULT 0,
  is_blacklisted INTEGER DEFAULT 0,
  is_admin INTEGER DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 2. Tabela `logins`

```sql
CREATE TABLE logins (
  id SERIAL PRIMARY KEY,
  tipo VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  senha VARCHAR(255) NOT NULL,
  cidade VARCHAR(255),
  is_sold INTEGER DEFAULT 0,
  added_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 3. Tabela `prices`

```sql
CREATE TABLE prices (
  id SERIAL PRIMARY KEY,
  price_name VARCHAR(255) NOT NULL,
  price_type VARCHAR(50) NOT NULL,
  price NUMERIC NOT NULL,
  description TEXT,
  category VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 4. Tabela `sold_balance`

```sql
CREATE TABLE sold_balance (
  id SERIAL PRIMARY KEY,
  owner BIGINT NOT NULL REFERENCES bot_users(telegram_id),
  type VARCHAR(50) NOT NULL,
  value NUMERIC NOT NULL,
  quantity INTEGER DEFAULT 1,
  add_balance_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 5. Tabela `bot_config`

```sql
CREATE TABLE bot_config (
  id SERIAL PRIMARY KEY,
  start_text TEXT,
  terms_text TEXT,
  support_user VARCHAR(255),
  channel_user VARCHAR(255),
  pay_auto VARCHAR(50) DEFAULT 'mercado pago',
  shop_layout_mode INTEGER DEFAULT 0,
  expiration_date TIMESTAMP,
  is_on INTEGER DEFAULT 1,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## 🎯 Configuração do Painel Web

### 1. Clonar e Instalar

```bash
cd lynx-admin
npm install
```

### 2. Configurar Variáveis de Ambiente

Crie um arquivo `.env.local`:

```env
NEXT_PUBLIC_SUPABASE_URL=https://seu-projeto.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=sua-chave-anon-aqui
```

**Como obter as credenciais:**
1. Acesse seu projeto Supabase
2. Vá para **Settings > API**
3. Copie `Project URL` e `anon public key`

### 3. Executar Localmente

```bash
npm run dev
```

Acesse em: `http://localhost:3000`

### 4. Build para Produção

```bash
npm run build
npm start
```

---

## 🤖 Configuração do Bot Telegram

### 1. Instalar Dependências

```bash
pip install pyrogram supabase python-dotenv
```

### 2. Criar Arquivo `.env`

```env
SUPABASE_URL=https://seu-projeto.supabase.co
SUPABASE_KEY=sua-chave-anon-aqui
BOT_TOKEN=seu-token-do-bot
API_ID=seu-api-id
API_HASH=seu-api-hash
```

### 3. Criar Módulo `supabase_db.py`

```python
import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)

# Funções de usuário
def get_user(telegram_id: int):
    response = supabase.table("bot_users").select("*").eq("telegram_id", telegram_id).execute()
    return response.data[0] if response.data else None

def create_user(telegram_id: int, name_user: str = None):
    supabase.table("bot_users").insert({
        "telegram_id": telegram_id,
        "name_user": name_user,
        "balance": 0
    }).execute()

def add_balance(telegram_id: int, amount: float):
    user = get_user(telegram_id)
    if user:
        new_balance = user["balance"] + amount
        supabase.table("bot_users").update({
            "balance": new_balance
        }).eq("telegram_id", telegram_id).execute()
        
        # Registrar venda
        supabase.table("sold_balance").insert({
            "owner": telegram_id,
            "type": "logins",
            "value": amount
        }).execute()

# Funções de logins
def get_logins(limit: int = 10):
    response = supabase.table("logins").select("*").eq("is_sold", 0).limit(limit).execute()
    return response.data

def add_login(tipo: str, email: str, senha: str, cidade: str):
    supabase.table("logins").insert({
        "tipo": tipo,
        "email": email,
        "senha": senha,
        "cidade": cidade
    }).execute()

def mark_login_sold(login_id: int):
    supabase.table("logins").update({
        "is_sold": 1
    }).eq("id", login_id).execute()

# Funções de configuração
def get_bot_config():
    response = supabase.table("bot_config").select("*").limit(1).execute()
    return response.data[0] if response.data else None

def update_bot_config(**kwargs):
    config = get_bot_config()
    if config:
        supabase.table("bot_config").update(kwargs).eq("id", config["id"]).execute()
    else:
        supabase.table("bot_config").insert(kwargs).execute()
```

### 4. Usar no Bot

```python
from supabase_db import get_user, add_balance, get_logins

# Exemplo: Processar compra
async def process_purchase(user_id: int, amount: float):
    user = get_user(user_id)
    if not user:
        create_user(user_id)
    
    add_balance(user_id, amount)
    await app.send_message(user_id, f"✅ Compra de R$ {amount} realizada!")
```

---

## 🔐 Segurança

### Boas Práticas

1. **Nunca commit `.env`** - Use `.env.local` localmente
2. **Chaves seguras** - Use chave `anon` para frontend, `service_role` apenas no backend
3. **RLS (Row Level Security)** - Configure políticas no Supabase
4. **HTTPS** - Sempre use conexões seguras em produção

### Exemplo de RLS

```sql
-- Apenas admins podem editar configurações
CREATE POLICY "Only admins can update config" ON bot_config
  FOR UPDATE USING (
    EXISTS (
      SELECT 1 FROM bot_users 
      WHERE telegram_id = auth.uid()::bigint 
      AND is_admin = 1
    )
  );
```

---

## 📱 Usando o Painel Web

### Funcionalidades

- **Dashboard**: Métricas em tempo real
- **Usuários**: Gerenciar saldos, banimentos, permissões
- **Estoque**: Adicionar/remover logins
- **Preços**: Configurar preços de produtos
- **Relatórios**: Visualizar histórico de vendas
- **Configurações**: Editar textos e parâmetros do bot

### Acesso

O painel está protegido por autenticação. Apenas usuários com `is_admin = 1` podem acessar.

---

## 🔄 Fluxo de Sincronização

### Quando um usuário compra no bot:

1. Bot valida a compra
2. Bot insere em `sold_balance`
3. Bot atualiza `bot_users.balance`
4. Painel web consulta dados em tempo real
5. Dashboard exibe métricas atualizadas

### Quando admin edita no painel:

1. Admin muda configuração
2. Painel atualiza `bot_config`
3. Bot lê configuração (ao iniciar ou periodicamente)
4. Bot aplica mudanças

---

## 🐛 Troubleshooting

### Erro: "Connection refused"
- Verifique se Supabase URL está correta
- Confirme que a chave é válida

### Erro: "Permission denied"
- Verifique políticas RLS no Supabase
- Use chave correta (anon para frontend)

### Dados não sincronizando
- Verifique se bot está usando `supabase_db.py`
- Confirme que as tabelas existem no Supabase
- Verifique logs do bot

---

## 📚 Recursos

- [Documentação Next.js](https://nextjs.org/docs)
- [Documentação Supabase](https://supabase.com/docs)
- [Pyrogram Docs](https://docs.pyrogram.org/)

---

## ✅ Checklist

- [ ] Criar projeto Supabase
- [ ] Criar tabelas no Supabase
- [ ] Configurar `.env.local` no painel
- [ ] Instalar dependências do bot
- [ ] Configurar `.env` do bot
- [ ] Testar sincronização
- [ ] Fazer deploy do painel
- [ ] Fazer deploy do bot

---

**Desenvolvido por:** Manus  
**Data:** 09 de Abril de 2026  
**Versão:** 1.0
