'use client'

import { DollarSign, Users, ShoppingCart, Package, Settings } from 'lucide-react'
import MetricCard from './MetricCard'

export default function Dashboard() {
  return (
    <div className="space-y-8">
      {/* Header */}
      <div className="flex justify-between items-center">
        <div>
          <h1 className="text-4xl font-bold text-slate-50">Dashboard</h1>
          <p className="text-slate-400 mt-2">Bem-vindo ao painel de controle</p>
        </div>
        <div className="flex gap-3">
          <button className="px-4 py-2 bg-slate-800 hover:bg-slate-700 text-slate-200 rounded-lg transition-colors">
            Atualizar
          </button>
          <button className="px-4 py-2 bg-purple-600 hover:bg-purple-700 text-white rounded-lg transition-colors flex items-center gap-2">
            <Settings className="w-4 h-4" />
            Manutenção
          </button>
        </div>
      </div>

      {/* Metrics Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-4">
        <MetricCard
          icon={DollarSign}
          label="Receita Total"
          value="R$ 5.663,04"
          change="+12.5%"
          color="green"
        />
        <MetricCard
          icon={Users}
          label="Total de Clientes"
          value="16"
          change="+3"
          color="blue"
        />
        <MetricCard
          icon={ShoppingCart}
          label="Total de Vendas"
          value="6"
          change="+2"
          color="purple"
        />
        <MetricCard
          icon={Package}
          label="Valor em Estoque"
          value="R$ 0,00"
          change="0"
          color="red"
          alert
        />
        <MetricCard
          icon={Package}
          label="Itens em Estoque"
          value="0"
          change="0"
          color="red"
          alert
        />
      </div>

      {/* Bot Status */}
      <div className="bg-slate-900 border border-slate-800 rounded-lg p-6">
        <div className="flex items-start justify-between">
          <div>
            <h2 className="text-xl font-bold text-slate-50 flex items-center gap-2">
              <div className="w-3 h-3 bg-green-500 rounded-full animate-pulse"></div>
              Status do Bot
            </h2>
            <p className="text-slate-400 text-sm mt-1">Controle o modo de manutenção do seu bot</p>
          </div>
          <button className="px-6 py-2 bg-yellow-500 hover:bg-yellow-600 text-slate-900 font-semibold rounded-lg transition-colors">
            ⚙️ Ativar Manutenção
          </button>
        </div>
        <div className="mt-4 p-3 bg-green-900/20 border border-green-800 rounded-lg flex items-center gap-2">
          <div className="w-2 h-2 bg-green-500 rounded-full"></div>
          <span className="text-green-300 text-sm">Online</span>
        </div>
      </div>

      {/* Financial Metrics */}
      <div className="bg-slate-900 border border-slate-800 rounded-lg p-6">
        <h2 className="text-xl font-bold text-slate-50 mb-6">💰 Métricas Financeiras</h2>
        <div className="grid grid-cols-2 md:grid-cols-5 gap-4">
          <div className="text-center">
            <p className="text-slate-400 text-sm">RECEITA HOJE</p>
            <p className="text-2xl font-bold text-slate-50 mt-2">R$ 0,00</p>
            <p className="text-xs text-slate-500 mt-1">0.00% vs ontem</p>
          </div>
          <div className="text-center">
            <p className="text-slate-400 text-sm">RECEITA SEMANAL</p>
            <p className="text-2xl font-bold text-slate-50 mt-2">R$ 10,00</p>
            <p className="text-xs text-green-400 mt-1">↑ 100% vs semana anterior</p>
          </div>
          <div className="text-center">
            <p className="text-slate-400 text-sm">RECEITA MENSAL</p>
            <p className="text-2xl font-bold text-slate-50 mt-2">R$ 10,00</p>
            <p className="text-xs text-green-400 mt-1">↑ 99.88% vs mês anterior</p>
          </div>
          <div className="text-center">
            <p className="text-slate-400 text-sm">TICKET MÉDIO</p>
            <p className="text-2xl font-bold text-slate-50 mt-2">R$ 31,17</p>
            <p className="text-xs text-red-400 mt-1">↓ 99.88% vs mês anterior</p>
          </div>
          <div className="text-center">
            <p className="text-slate-400 text-sm">SALDO DM CONTAS</p>
            <p className="text-2xl font-bold text-slate-50 mt-2">R$ 9.985,00</p>
            <p className="text-xs text-slate-500 mt-1">Previsão: R$ 92,14</p>
          </div>
        </div>
      </div>

      {/* Top Products and Buyers */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Top 5 Produtos */}
        <div className="bg-slate-900 border border-slate-800 rounded-lg p-6">
          <h3 className="text-lg font-bold text-slate-50 mb-4">🏆 Top 5 Produtos</h3>
          <div className="space-y-3">
            {[
              { name: 'NETFLIX PREMIUM', value: 'R$ 160,00' },
              { name: 'Spotify Premium', value: 'R$ 120,00' },
              { name: 'Disney+', value: 'R$ 80,00' },
              { name: 'HBO Max', value: 'R$ 60,00' },
              { name: 'Amazon Prime', value: 'R$ 40,00' },
            ].map((product, i) => (
              <div key={i} className="flex justify-between items-center p-2 hover:bg-slate-800 rounded">
                <span className="text-slate-300">{product.name}</span>
                <span className="text-green-400 font-semibold">{product.value}</span>
              </div>
            ))}
          </div>
        </div>

        {/* Top 5 Compradores */}
        <div className="bg-slate-900 border border-slate-800 rounded-lg p-6">
          <h3 className="text-lg font-bold text-slate-50 mb-4">👥 Top 5 Compradores</h3>
          <div className="space-y-3">
            {[
              { name: 'User 6918907252', value: 'R$ 160,00' },
              { name: 'User 1234567890', value: 'R$ 120,00' },
              { name: 'User 9876543210', value: 'R$ 80,00' },
              { name: 'User 5555555555', value: 'R$ 60,00' },
              { name: 'User 3333333333', value: 'R$ 40,00' },
            ].map((buyer, i) => (
              <div key={i} className="flex justify-between items-center p-2 hover:bg-slate-800 rounded">
                <span className="text-slate-300">{buyer.name}</span>
                <span className="text-green-400 font-semibold">{buyer.value}</span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  )
}
