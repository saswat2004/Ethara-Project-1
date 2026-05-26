"""
generate_structure.py

This script sets up the base file structure matching the provided Next.js workspace.

Run:
python generate_structure.py
"""

import os

WORKSPACE_FILES = {
    # --- Root Configuration Files ---
    ".gitignore": """
# See https://help.github.com/articles/ignoring-files/ for more about ignoring files.

# dependencies
/node_modules
/.pnp
.pnp.*
.yarn/*
!.yarn/patches
!.yarn/plugins
!.yarn/releases
!.yarn/versions

# testing
/coverage

# next.js
/.next/
/out/

# production
/build

# misc
.DS_Store
*.pem

# debug
npm-debug.log*
yarn-debug.log*
yarn-error.log*
.pnpm-debug.log*

# env files (can opt-in for committing if needed)
.env*

# vercel
.vercel

# typescript
*.tsbuildinfo
next-env.d.ts

""",

    "AGENTS.md": """
<!-- BEGIN:nextjs-agent-rules -->
# This is NOT the Next.js you know

This version has breaking changes — APIs, conventions, and file structure may all differ from your training data. Read the relevant guide in `node_modules/next/dist/docs/` before writing any code. Heed deprecation notices.
<!-- END:nextjs-agent-rules -->

""",

    "CLAUDE.md": """
@AGENTS.md

""",

    "eslint.config.mjs": """
import { defineConfig, globalIgnores } from "eslint/config";
import nextVitals from "eslint-config-next/core-web-vitals";
import nextTs from "eslint-config-next/typescript";

const eslintConfig = defineConfig([
  ...nextVitals,
  ...nextTs,
  // Override default ignores of eslint-config-next.
  globalIgnores([
    // Default ignores of eslint-config-next:
    ".next/**",
    "out/**",
    "build/**",
    "next-env.d.ts",
  ]),
]);

export default eslintConfig;

""",

    "next-env.d.ts": """
/// <reference types="next" />
/// <reference types="next/image-types/global" />
import "./.next/types/routes.d.ts";

// NOTE: This file should not be edited
// see https://nextjs.org/docs/app/api-reference/config/typescript for more information.

""",

    "next.config.ts": """
import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  /* config options here */
};

export default nextConfig;

""",

    "package.json": """
{
  "name": "advanced-calculator",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "eslint"
  },
  "dependencies": {
    "clsx": "^2.1.1",
    "framer-motion": "^12.40.0",
    "lucide-react": "^1.16.0",
    "mathjs": "^15.2.0",
    "next": "16.2.6",
    "react": "19.2.4",
    "react-dom": "19.2.4",
    "recharts": "^3.8.1",
    "tailwind-merge": "^3.6.0"
  },
  "devDependencies": {
    "@tailwindcss/postcss": "^4",
    "@types/node": "^20",
    "@types/react": "^19",
    "@types/react-dom": "^19",
    "eslint": "^9",
    "eslint-config-next": "16.2.6",
    "tailwindcss": "^4",
    "typescript": "^5"
  }
}

""",

    "postcss.config.mjs": """
const config = {
  plugins: {
    "@tailwindcss/postcss": {},
  },
};

export default config;

""",

    "README.md": """
This is a [Next.js](https://nextjs.org) project bootstrapped with [`create-next-app`](https://nextjs.org/docs/app/api-reference/cli/create-next-app).

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/app/building-your-application/optimizing/fonts) to automatically optimize and load [Geist](https://vercel.com/font), a new font family for Vercel.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/app/building-your-application/deploying) for more details.

""",

    "tsconfig.json": """
{
  "compilerOptions": {
    "target": "ES2017",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "react-jsx",
    "incremental": true,
    "plugins": [
      {
        "name": "next"
      }
    ],
    "baseUrl": ".",
    "ignoreDeprecations": "6.0",
    "paths": {
      "@/*": ["./*"]
    }
  },
  "include": [
    "next-env.d.ts",
    "**/*.ts",
    "**/*.tsx",
    ".next/types/**/*.ts",
    ".next/dev/types/**/*.ts",
    "**/*.mts"
  ],
  "exclude": ["node_modules"]
}

""",

    # --- App Directory ---
    "app/page.tsx": """
'use client';

import { useState } from 'react';
import CalculatorCore from '@/components/CalculatorCore';
import HistoryPanel from '@/components/HistoryPanel';
import dynamic from 'next/dynamic';
import { Menu, X } from 'lucide-react';

const GraphingModule = dynamic(() => import('@/components/GraphingModule'), {
  loading: () => <p className="p-4 animate-pulse text-slate-400">Loading Graphing Engine...</p>,
  ssr: false,
});

export default function CalculatorApp() {
  const [history, setHistory] = useState<{ eq: string; res: string }[]>([]);
  const [activeTab, setActiveTab] = useState<'calc' | 'graph'>('calc');
  const [showMobileHistory, setShowMobileHistory] = useState(false);

  const addToHistory = (eq: string, res: string) => {
    setHistory((prev) => [{ eq, res }, ...prev]);
  };

  return (
    <main className="flex h-screen w-full bg-slate-950 text-slate-100 font-sans overflow-hidden">
      <div className="hidden md:block">
        <HistoryPanel history={history} />
      </div>

      {showMobileHistory && (
        <div className="absolute inset-0 z-50 bg-slate-950 flex md:hidden">
          <div className="flex-1 w-full relative">
            <button
              onClick={() => setShowMobileHistory(false)}
              className="absolute top-4 right-4 p-2 bg-slate-800 hover:bg-slate-700 rounded-md text-white transition-colors"
              aria-label="Close history"
            >
              <X size={24} />
            </button>
            <HistoryPanel history={history} className="w-full border-none" />
          </div>
        </div>
      )}

      <section className="flex-1 flex flex-col relative">
        <header className="flex flex-col sm:flex-row gap-2 md:gap-4 p-4 border-b border-slate-800 items-center justify-between">
          <div className="flex gap-2 md:gap-4">
            <button
              onClick={() => setActiveTab('calc')}
              className={`px-3 py-2 md:px-4 rounded-md transition-colors text-sm md:text-base ${activeTab === 'calc' ? 'bg-blue-600' : 'hover:bg-slate-800'}`}
            >
              Calculator
            </button>
            <button
              onClick={() => setActiveTab('graph')}
              className={`px-3 py-2 md:px-4 rounded-md transition-colors text-sm md:text-base ${activeTab === 'graph' ? 'bg-blue-600' : 'hover:bg-slate-800'}`}
            >
              Graphing
            </button>
          </div>

          <button
            onClick={() => setShowMobileHistory(true)}
            className="md:hidden p-2 bg-slate-800 hover:bg-slate-700 rounded-md text-slate-200 transition-colors"
            aria-label="Toggle history"
          >
            <Menu size={20} />
          </button>
        </header>

        <div className="flex-1 overflow-auto p-4 flex items-center justify-center">
          {activeTab === 'calc' ? (
            <CalculatorCore onCalculated={addToHistory} />
          ) : (
            <GraphingModule />
          )}
        </div>
      </section>
    </main>
  );
}

""",

    "app/layout.tsx": """
import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "Create Next App",
  description: "Generated by create next app",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html
      lang="en"
      className={`${geistSans.variable} ${geistMono.variable} h-full antialiased`}
    >
      <body className="min-h-full flex flex-col">{children}</body>
    </html>
  );
}

""",

    "app/globals.css": """
@import "tailwindcss";

:root {
  --background: #ffffff;
  --foreground: #171717;
}

@theme inline {
  --color-background: var(--background);
  --color-foreground: var(--foreground);
  --font-sans: var(--font-geist-sans);
  --font-mono: var(--font-geist-mono);
}

@media (prefers-color-scheme: dark) {
  :root {
    --background: #0a0a0a;
    --foreground: #ededed;
  }
}

body {
  background: var(--background);
  color: var(--foreground);
  font-family: Arial, Helvetica, sans-serif;
}

""",

}

def generate_workspace():
    root_dir = os.getcwd()

    for relative_path, content in WORKSPACE_FILES.items():
        file_path = os.path.join(root_dir, relative_path)
        folder_path = os.path.dirname(file_path)

        os.makedirs(folder_path, exist_ok=True)

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content.strip() + "\n")

        print(f"Created: {relative_path}")

    print("\nAdvanced Calculator project structure generated successfully.")

if __name__ == "__main__":
    generate_workspace()