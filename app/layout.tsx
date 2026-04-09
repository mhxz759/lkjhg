import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'Lynx Dev - Painel Administrativo',
  description: 'Painel de controle para gerenciar seu bot de vendas',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="pt-BR">
      <body className="bg-slate-950 text-slate-50">
        {children}
      </body>
    </html>
  )
}
