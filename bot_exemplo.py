"""
Exemplo de integração do Bot Telegram com Supabase
"""

from pyrogram import Client, filters
from supabase_bot import (
    get_user, create_user, add_balance, get_logins,
    get_bot_config, get_metrics
)
import os
from dotenv import load_dotenv

load_dotenv()

# Inicializar bot
app = Client(
    "bot_session",
    api_id=int(os.getenv("API_ID")),
    api_hash=os.getenv("API_HASH"),
    bot_token=os.getenv("BOT_TOKEN")
)

# ============================================================================
# COMANDOS DO BOT
# ============================================================================

@app.on_message(filters.command("start"))
async def start(client, message):
    """Comando /start"""
    user_id = message.from_user.id
    
    # Criar usuário se não existir
    user = get_user(user_id)
    if not user:
        create_user(user_id, message.from_user.first_name, message.from_user.username)
    
    # Obter configuração do bot
    config = get_bot_config()
    start_text = config["start_text"] if config else "Bem-vindo ao bot!"
    
    await message.reply(start_text)

@app.on_message(filters.command("saldo"))
async def balance(client, message):
    """Comando /saldo - Ver saldo"""
    user_id = message.from_user.id
    user = get_user(user_id)
    
    if not user:
        await message.reply("❌ Usuário não encontrado")
        return
    
    saldo = user["balance"]
    await message.reply(f"💰 Seu saldo: R$ {saldo:.2f}")

@app.on_message(filters.command("logins"))
async def list_logins(client, message):
    """Comando /logins - Listar logins disponíveis"""
    logins = get_logins(limit=5)
    
    if not logins:
        await message.reply("❌ Nenhum login disponível no momento")
        return
    
    text = "📋 Logins disponíveis:\n\n"
    for login in logins:
        text += f"• {login['tipo']}: {login['email']}\n"
    
    await message.reply(text)

@app.on_message(filters.command("comprar"))
async def buy(client, message):
    """Comando /comprar - Simular compra"""
    user_id = message.from_user.id
    
    # Simular compra de R$ 50
    amount = 50.0
    add_balance(user_id, amount)
    
    await message.reply(f"✅ Compra de R$ {amount:.2f} realizada com sucesso!")

@app.on_message(filters.command("metricas"))
async def metrics(client, message):
    """Comando /metricas - Ver métricas (admin)"""
    user_id = message.from_user.id
    user = get_user(user_id)
    
    if not user or not user["is_admin"]:
        await message.reply("❌ Você não tem permissão")
        return
    
    metrics_data = get_metrics()
    
    text = "📊 Métricas do Bot:\n\n"
    text += f"👥 Total de usuários: {metrics_data['total_users']}\n"
    text += f"💰 Total de vendas: R$ {metrics_data['total_sales']:.2f}\n"
    text += f"📦 Logins disponíveis: {metrics_data['total_logins']}\n"
    
    await message.reply(text)

# ============================================================================
# INICIAR BOT
# ============================================================================

if __name__ == "__main__":
    print("🤖 Bot iniciando...")
    app.run()
