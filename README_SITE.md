# 🌐 Painel Lynx Dev - Next.js

Painel administrativo moderno para gerenciar seu bot de vendas Telegram.

## 📦 Arquivos

- **app/** - Páginas e layout do Next.js
- **components/** - Componentes React
- **utils/supabase/** - Clientes Supabase
- **package.json** - Dependências
- **INTEGRACAO_SUPABASE.md** - Guia de integração
- **supabase_bot.py** - Módulo do bot (para referência)

## 🚀 Instalação

### 1. Instalar dependências

```bash
npm install
```

### 2. Configurar variáveis de ambiente

Crie um arquivo `.env.local`:

```env
NEXT_PUBLIC_SUPABASE_URL=https://seu-projeto.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=sua-chave-anon-aqui
```

### 3. Executar localmente

```bash
npm run dev
```

Acesse em: `http://localhost:3000`

## 🏗️ Build para Produção

```bash
npm run build
npm start
```

## 📊 Funcionalidades

- **Dashboard** - Métricas em tempo real
- **Usuários** - Gerenciar saldos, banimentos, permissões
- **Estoque** - Adicionar/remover logins
- **Preços** - Configurar preços de produtos
- **Relatórios** - Visualizar histórico de vendas
- **Configurações** - Editar textos e parâmetros do bot

## 🎨 Design

Design escuro moderno "Lynx Dev" com:
- Sidebar de navegação lateral
- Cards com métricas destacadas
- Acentos coloridos
- Interface responsiva

## 🔗 Integração com Supabase

O painel se conecta ao Supabase para sincronizar dados em tempo real com o bot.

Tabelas necessárias:
- `bot_users` - Usuários
- `logins` - Estoque de contas
- `prices` - Preços
- `sold_balance` - Histórico de vendas
- `bot_config` - Configurações

## 🔐 Segurança

- Nunca commit `.env.local`
- Use chave `anon` para o frontend
- Configure RLS no Supabase
- Sempre use HTTPS em produção

## 📚 Documentação

Consulte `INTEGRACAO_SUPABASE.md` para guia completo de integração.

## 🚀 Deploy

### Vercel (Recomendado)

```bash
npm install -g vercel
vercel
```

### Outras plataformas

O Next.js pode ser deployado em:
- Netlify
- Railway
- Render
- AWS
- Google Cloud
- Azure

---

**Versão:** 1.0  
**Data:** 09 de Abril de 2026
