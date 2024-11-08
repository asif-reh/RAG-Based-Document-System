import { Metadata } from 'next';
import { DashboardHeader } from '@/components/dashboard-header';
import { NoteEditor } from '@/components/note-editor';
import { getServerSession } from 'next-auth';
import { authOptions } from '@/lib/auth';

export const metadata: Metadata = {
  title: 'Dashboard - AI Notes',
  description: 'Manage your notes and get AI-powered insights',
};

export default async function DashboardPage() {
  const session = await getServerSession(authOptions);

  return (
    <div className="flex min-h-screen flex-col">
      <DashboardHeader user={session?.user} />
      <main className="flex-1 container mx-auto px-4 py-8">
        <NoteEditor />
      </main>
    </div>
  );
}