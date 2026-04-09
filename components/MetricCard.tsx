'use client'

import { LucideIcon, AlertCircle } from 'lucide-react'

interface MetricCardProps {
  icon: LucideIcon
  label: string
  value: string
  change: string
  color: 'green' | 'blue' | 'purple' | 'red'
  alert?: boolean
}

export default function MetricCard({
  icon: Icon,
  label,
  value,
  change,
  color,
  alert,
}: MetricCardProps) {
  const bgColors = {
    green: 'bg-green-900/20 border-green-800',
    blue: 'bg-blue-900/20 border-blue-800',
    purple: 'bg-purple-900/20 border-purple-800',
    red: 'bg-red-900/20 border-red-800',
  }

  const iconColors = {
    green: 'bg-green-600',
    blue: 'bg-blue-600',
    purple: 'bg-purple-600',
    red: 'bg-red-600',
  }

  const textColors = {
    green: 'text-green-400',
    blue: 'text-blue-400',
    purple: 'text-purple-400',
    red: 'text-red-400',
  }

  return (
    <div className={`bg-slate-900 border rounded-lg p-4 ${bgColors[color]}`}>
      <div className="flex items-start justify-between">
        <div>
          <p className="text-slate-400 text-xs font-medium">{label}</p>
          <p className="text-2xl font-bold text-slate-50 mt-2">{value}</p>
          {alert ? (
            <div className="flex items-center gap-1 mt-2">
              <AlertCircle className="w-3 h-3 text-red-400" />
              <p className={`text-xs font-semibold ${textColors[color]}`}>{change} em alerta</p>
            </div>
          ) : (
            <p className={`text-xs font-semibold ${textColors[color]} mt-2`}>{change}</p>
          )}
        </div>
        <div className={`${iconColors[color]} p-3 rounded-lg`}>
          <Icon className="w-6 h-6 text-white" />
        </div>
      </div>
    </div>
  )
}
