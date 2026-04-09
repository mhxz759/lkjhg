'use client'

import { useState } from 'react'
import Sidebar from '@/components/Sidebar'
import Dashboard from '@/components/Dashboard'
import Users from '@/components/Users'
import Logins from '@/components/Logins'
import Prices from '@/components/Prices'
import Reports from '@/components/Reports'
import Settings from '@/components/Settings'

export default function Home() {
  const [currentPage, setCurrentPage] = useState('dashboard')

  const renderPage = () => {
    switch (currentPage) {
      case 'dashboard':
        return <Dashboard />
      case 'users':
        return <Users />
      case 'logins':
        return <Logins />
      case 'prices':
        return <Prices />
      case 'reports':
        return <Reports />
      case 'settings':
        return <Settings />
      default:
        return <Dashboard />
    }
  }

  return (
    <div className="flex h-screen bg-slate-950 overflow-hidden">
      <Sidebar currentPage={currentPage} setCurrentPage={setCurrentPage} />
      <main className="flex-1 overflow-auto bg-slate-950">
        <div className="p-8">
          {renderPage()}
        </div>
      </main>
    </div>
  )
}
