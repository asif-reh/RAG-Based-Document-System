import { Metadata } from 'next';
import Link from 'next/link';
import { Button } from '@/components/ui/button';
import { PenLine } from 'lucide-react';

export const metadata: Metadata = {
  title: 'AI Notes - Smart Digital Diary',
  description: 'Transform your thoughts with AI-powered note-taking',
};

export default function Home() {
  return (
    <div className="flex min-h-screen flex-col">
      <header className="px-4 lg:px-6 h-14 flex items-center">
        <Link className="flex items-center justify-center" href="/">
          <PenLine className="h-6 w-6" />
          <span className="ml-2 text-lg font-semibold">AI Notes</span>
        </Link>
        <nav className="ml-auto flex gap-4 sm:gap-6">
          <Link className="text-sm font-medium hover:underline underline-offset-4" href="/sign-in">
            Sign In
          </Link>
        </nav>
      </header>
      <main className="flex-1">
        <section className="w-full py-12 md:py-24 lg:py-32 xl:py-48">
          <div className="container px-4 md:px-6">
            <div className="flex flex-col items-center space-y-4 text-center">
              <div className="space-y-2">
                <h1 className="text-3xl font-bold tracking-tighter sm:text-4xl md:text-5xl lg:text-6xl/none">
                  Your Thoughts, Enhanced by AI
                </h1>
                <p className="mx-auto max-w-[700px] text-gray-500 md:text-xl dark:text-gray-400">
                  Transform your note-taking experience with AI-powered insights. Write smarter, remember better.
                </p>
              </div>
              <div className="space-x-4">
                <Link href="/sign-in">
                  <Button>Get Started</Button>
                </Link>
              </div>
            </div>
          </div>
        </section>
        <section className="w-full py-12 md:py-24 lg:py-32 bg-gray-100 dark:bg-gray-800">
          <div className="container px-4 md:px-6">
            <div className="grid gap-10 sm:grid-cols-2 lg:grid-cols-3">
              <div className="flex flex-col items-center space-y-4 text-center">
                <div className="p-4 bg-white rounded-full dark:bg-gray-900">
                  <PenLine className="h-6 w-6" />
                </div>
                <h2 className="text-xl font-bold">Smart Writing Assistant</h2>
                <p className="text-gray-500 dark:text-gray-400">
                  Get AI-powered suggestions as you write to improve clarity and style.
                </p>
              </div>
              <div className="flex flex-col items-center space-y-4 text-center">
                <div className="p-4 bg-white rounded-full dark:bg-gray-900">
                  <PenLine className="h-6 w-6" />
                </div>
                <h2 className="text-xl font-bold">Organized Thoughts</h2>
                <p className="text-gray-500 dark:text-gray-400">
                  Keep your notes organized with smart categorization and tagging.
                </p>
              </div>
              <div className="flex flex-col items-center space-y-4 text-center">
                <div className="p-4 bg-white rounded-full dark:bg-gray-900">
                  <PenLine className="h-6 w-6" />
                </div>
                <h2 className="text-xl font-bold">Daily Insights</h2>
                <p className="text-gray-500 dark:text-gray-400">
                  Get AI-generated insights from your daily entries.
                </p>
              </div>
            </div>
          </div>
        </section>
      </main>
      <footer className="flex flex-col gap-2 sm:flex-row py-6 w-full shrink-0 items-center px-4 md:px-6 border-t">
        <p className="text-xs text-gray-500 dark:text-gray-400">
          © 2024 AI Notes. All rights reserved.
        </p>
        <nav className="sm:ml-auto flex gap-4 sm:gap-6">
          <Link className="text-xs hover:underline underline-offset-4" href="#">
            Terms of Service
          </Link>
          <Link className="text-xs hover:underline underline-offset-4" href="#">
            Privacy
          </Link>
        </nav>
      </footer>
    </div>
  );
}