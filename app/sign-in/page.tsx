import { Metadata } from 'next';
import { Button } from '@/components/ui/button';
import { PenLine } from 'lucide-react';
import Link from 'next/link';
import { GoogleSignInButton } from '@/components/auth-buttons';

export const metadata: Metadata = {
  title: 'Sign In - AI Notes',
  description: 'Sign in to your AI Notes account',
};

export default function SignInPage() {
  return (
    <div className="flex min-h-screen flex-col">
      <div className="flex min-h-screen items-center justify-center">
        <div className="mx-auto flex w-full flex-col justify-center space-y-6 sm:w-[350px]">
          <div className="flex flex-col space-y-2 text-center">
            <Link href="/" className="mx-auto">
              <PenLine className="h-8 w-8" />
            </Link>
            <h1 className="text-2xl font-semibold tracking-tight">Welcome back</h1>
            <p className="text-sm text-muted-foreground">
              Sign in to your account to continue
            </p>
          </div>
          <GoogleSignInButton />
          <p className="px-8 text-center text-sm text-muted-foreground">
            By clicking continue, you agree to our{' '}
            <Link
              href="/terms"
              className="hover:text-brand underline underline-offset-4"
            >
              Terms of Service
            </Link>{' '}
            and{' '}
            <Link
              href="/privacy"
              className="hover:text-brand underline underline-offset-4"
            >
              Privacy Policy
            </Link>
            .
          </p>
        </div>
      </div>
    </div>
  );
}