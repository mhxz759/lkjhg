"""
Módulo de integração Supabase para Bot Telegram
Substitui operações SQLite pelo Supabase
"""

import os
from datetime import datetime
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

# Inicializar cliente Supabase
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)

# ============================================================================
# FUNÇÕES DE USUÁRIOS
# ============================================================================

def get_user(telegram_id: int):
    """Buscar usuário por Telegram ID"""
    try:
        response = supabase.table("bot_users").select("*").eq("telegram_id", telegram_id).execute()
        return response.data[0] if response.data else None
    except Exception as e:
        print(f"Erro ao buscar usuário: {e}")
        return None

def create_user(telegram_id: int, name_user: str = None, username: str = None):
    """Criar novo usuário"""
    try:
        supabase.table("bot_users").insert({
            "telegram_id": telegram_id,
            "name_user": name_user,
            "username": username,
            "balance": 0,
            "is_blacklisted": 0,
            "is_admin": 0
        }).execute()
        return True
    except Exception as e:
        print(f"Erro ao criar usuário: {e}")
        return False

def get_user_balance(telegram_id: int) -> float:
    """Obter saldo do usuário"""
    user = get_user(telegram_id)
    return user["balance"] if user else 0

def add_balance(telegram_id: int, amount: float, type_: str = "logins"):
    """Adicionar saldo ao usuário e registrar venda"""
    try:
        user = get_user(telegram_id)
        
        if not user:
            create_user(telegram_id)
            user = get_user(telegram_id)
        
        if user:
            new_balance = user["balance"] + amount
            supabase.table("bot_users").update({
                "balance": new_balance,
                "updated_at": datetime.now().isoformat()
            }).eq("telegram_id", telegram_id).execute()
            
            # Registrar venda
            supabase.table("sold_balance").insert({
                "owner": telegram_id,
                "type": type_,
                "value": amount,
                "quantity": 1
            }).execute()
            return True
    except Exception as e:
        print(f"Erro ao adicionar saldo: {e}")
        return False

def set_user_balance(telegram_id: int, amount: float):
    """Definir saldo do usuário (admin)"""
    try:
        supabase.table("bot_users").update({
            "balance": amount,
            "updated_at": datetime.now().isoformat()
        }).eq("telegram_id", telegram_id).execute()
        return True
    except Exception as e:
        print(f"Erro ao definir saldo: {e}")
        return False

def blacklist_user(telegram_id: int, is_blacklisted: int = 1):
    """Banir ou desbanir usuário"""
    try:
        supabase.table("bot_users").update({
            "is_blacklisted": is_blacklisted,
            "updated_at": datetime.now().isoformat()
        }).eq("telegram_id", telegram_id).execute()
        return True
    except Exception as e:
        print(f"Erro ao atualizar blacklist: {e}")
        return False

def promote_to_admin(telegram_id: int):
    """Promover usuário a administrador"""
    try:
        supabase.table("bot_users").update({
            "is_admin": 1,
            "updated_at": datetime.now().isoformat()
        }).eq("telegram_id", telegram_id).execute()
        return True
    except Exception as e:
        print(f"Erro ao promover admin: {e}")
        return False

# ============================================================================
# FUNÇÕES DE LOGINS/ESTOQUE
# ============================================================================

def get_logins(tipo: str = None, limit: int = 10):
    """Listar logins disponíveis"""
    try:
        query = supabase.table("logins").select("*").eq("is_sold", 0)
        
        if tipo:
            query = query.eq("tipo", tipo)
        
        response = query.limit(limit).execute()
        return response.data
    except Exception as e:
        print(f"Erro ao listar logins: {e}")
        return []

def get_login_by_id(login_id: int):
    """Obter login específico"""
    try:
        response = supabase.table("logins").select("*").eq("id", login_id).execute()
        return response.data[0] if response.data else None
    except Exception as e:
        print(f"Erro ao obter login: {e}")
        return None

def add_login(tipo: str, email: str, senha: str, cidade: str):
    """Adicionar novo login"""
    try:
        supabase.table("logins").insert({
            "tipo": tipo,
            "email": email,
            "senha": senha,
            "cidade": cidade,
            "is_sold": 0
        }).execute()
        return True
    except Exception as e:
        print(f"Erro ao adicionar login: {e}")
        return False

def delete_login(login_id: int):
    """Remover login"""
    try:
        supabase.table("logins").delete().eq("id", login_id).execute()
        return True
    except Exception as e:
        print(f"Erro ao remover login: {e}")
        return False

def mark_login_sold(login_id: int):
    """Marcar login como vendido"""
    try:
        supabase.table("logins").update({
            "is_sold": 1,
            "updated_at": datetime.now().isoformat()
        }).eq("id", login_id).execute()
        return True
    except Exception as e:
        print(f"Erro ao marcar login como vendido: {e}")
        return False

# ============================================================================
# FUNÇÕES DE PREÇOS
# ============================================================================

def get_prices(price_type: str = None):
    """Listar preços"""
    try:
        query = supabase.table("prices").select("*")
        
        if price_type:
            query = query.eq("price_type", price_type)
        
        response = query.execute()
        return response.data
    except Exception as e:
        print(f"Erro ao listar preços: {e}")
        return []

def get_price(price_name: str, price_type: str):
    """Obter preço específico"""
    try:
        response = supabase.table("prices").select("*").eq("price_name", price_name).eq("price_type", price_type).execute()
        return response.data[0] if response.data else None
    except Exception as e:
        print(f"Erro ao obter preço: {e}")
        return None

def add_price(price_name: str, price_type: str, price: float, description: str = ""):
    """Adicionar novo preço"""
    try:
        supabase.table("prices").insert({
            "price_name": price_name,
            "price_type": price_type,
            "price": price,
            "description": description
        }).execute()
        return True
    except Exception as e:
        print(f"Erro ao adicionar preço: {e}")
        return False

# ============================================================================
# FUNÇÕES DE CONFIGURAÇÃO
# ============================================================================

def get_bot_config():
    """Obter configurações do bot"""
    try:
        response = supabase.table("bot_config").select("*").limit(1).execute()
        return response.data[0] if response.data else None
    except Exception as e:
        print(f"Erro ao obter configurações: {e}")
        return None

def update_bot_config(**kwargs):
    """Atualizar configurações do bot"""
    try:
        config = get_bot_config()
        
        kwargs["updated_at"] = datetime.now().isoformat()
        
        if config:
            supabase.table("bot_config").update(kwargs).eq("id", config["id"]).execute()
        else:
            supabase.table("bot_config").insert(kwargs).execute()
        return True
    except Exception as e:
        print(f"Erro ao atualizar configurações: {e}")
        return False

# ============================================================================
# FUNÇÕES DE MÉTRICAS
# ============================================================================

def get_metrics():
    """Obter métricas para o dashboard"""
    try:
        # Total de usuários
        users_response = supabase.table("bot_users").select("COUNT(*)").execute()
        total_users = len(users_response.data) if users_response.data else 0
        
        # Total de vendas
        sales_response = supabase.table("sold_balance").select("value").execute()
        total_sales = sum(item["value"] for item in sales_response.data) if sales_response.data else 0
        
        # Total de logins disponíveis
        logins_response = supabase.table("logins").select("COUNT(*)").eq("is_sold", 0).execute()
        total_logins = len(logins_response.data) if logins_response.data else 0
        
        return {
            "total_users": total_users,
            "total_sales": total_sales,
            "total_logins": total_logins
        }
    except Exception as e:
        print(f"Erro ao obter métricas: {e}")
        return {
            "total_users": 0,
            "total_sales": 0,
            "total_logins": 0
        }

def get_sales_history(limit: int = 20):
    """Obter histórico de vendas"""
    try:
        response = supabase.table("sold_balance").select("*").order(
            "add_balance_date",
            desc=True
        ).limit(limit).execute()
        return response.data
    except Exception as e:
        print(f"Erro ao obter histórico de vendas: {e}")
        return []
