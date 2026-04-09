# 🚀 Lynx Dev - Painel Administrativo Web

Painel administrativo moderno para gerenciar seu bot de vendas Telegram, com integração completa ao Supabase.

## ✨ Funcionalidades

- **Dashboard**: Métricas em tempo real com cards de receita, clientes, vendas e estoque
- **Usuários**: Gerenciar saldos, banimentos e permissões de admin
- **Estoque**: Adicionar, remover e visualizar logins disponíveis
- **Preços**: Configurar preços de produtos
- **Relatórios**: Visualizar histórico completo de vendas
- **Configurações**: Editar textos, gateway de pagamento e parâmetros do bot

## 🎨 Design

Design escuro moderno "Lynx Dev" com:
- Sidebar de navegação lateral
- Cards com métricas destacadas
- Acentos coloridos (purple, blue, green)
- Interface responsiva
- Componentes reutilizáveis

## 🛠️ Tecnologias

- **Next.js 16** - Framework React
- **TypeScript** - Tipagem segura
- **Tailwind CSS 4** - Estilos
- **Supabase** - Banco de dados
- **Lucide React** - Ícones

## 📦 Instalação

### 1. Clonar o projeto

```bash
git clone <seu-repositorio>
cd lynx-admin
```

### 2. Instalar dependências

```bash
npm install
```

### 3. Configurar variáveis de ambiente

Crie um arquivo `.env.local`:

```env
NEXT_PUBLIC_SUPABASE_URL=https://seu-projeto.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=sua-chave-anon-aqui
```

### 4. Executar localmente

```bash
npm run dev
```

Acesse em: `http://localhost:3000`

## 🚀 Deploy

### Build para produção

```bash
npm run build
npm start
```

### Deploy no Vercel

```bash
npm install -g vercel
vercel
```

## 🤖 Integração com Bot Telegram

### 1. Instalar dependências do bot

```bash
pip install pyrogram supabase python-dotenv
```

### 2. Configurar `.env` do bot

```env
SUPABASE_URL=https://seu-projeto.supabase.co
SUPABASE_KEY=sua-chave-anon-aqui
BOT_TOKEN=seu-token-do-bot
API_ID=seu-api-id
API_HASH=seu-api-hash
```

### 3. Usar o módulo `supabase_bot.py`

```python
from supabase_bot import get_user, add_balance, get_logins

# Exemplo: Processar compra
async def process_purchase(user_id: int, amount: float):
    user = get_user(user_id)
    if not user:
        create_user(user_id)
    
    add_balance(user_id, amount)
    await app.send_message(user_id, f"✅ Compra de R$ {amount} realizada!")
```

## 📊 Estrutura do Banco de Dados

O Supabase deve ter as seguintes tabelas:

- `bot_users` - Usuários do bot
- `logins` - Estoque de contas
- `prices` - Preços de produtos
- `sold_balance` - Histórico de vendas
- `bot_config` - Configurações do bot

Veja `INTEGRACAO_SUPABASE.md` para o SQL completo.

## 📚 Documentação

- **INTEGRACAO_SUPABASE.md** - Guia completo de integração
- **supabase_bot.py** - Módulo Python para o bot

## 🔐 Segurança

- Nunca commit `.env.local`
- Use chave `anon` para o frontend
- Configure RLS no Supabase
- Sempre use HTTPS em produção

## 🐛 Troubleshooting

### Erro: "Connection refused"
- Verifique se Supabase URL está correta
- Confirme que a chave é válida

### Erro: "Permission denied"
- Verifique políticas RLS no Supabase
- Use chave correta

### Dados não sincronizando
- Verifique se bot está usando `supabase_bot.py`
- Confirme que as tabelas existem no Supabase

## 📞 Suporte

Para dúvidas, consulte:
- [Documentação Next.js](https://nextjs.org/docs)
- [Documentação Supabase](https://supabase.com/docs)
- [Pyrogram Docs](https://docs.pyrogram.org/)

## 📄 Licença

MIT

---

**Desenvolvido por:** Manus  
**Data:** 09 de Abril de 2026  
**Versão:** 1.0
