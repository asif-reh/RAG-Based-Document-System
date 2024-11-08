'use client';

import { signIn } from 'next-auth/react';
import { Button } from '@/components/ui/button';

export function GoogleSignInButton() {
  return (
    <Button
      onClick={() => signIn('google', { callbackUrl: '/dashboard' })}
      variant="outline"
      className="w-full"
    >
      Continue with Google
    </Button>
  );
}