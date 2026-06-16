<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { Head } from '@inertiajs/vue3';
import { FlaskConical, Rocket, CheckCircle2, AlertCircle, Loader2 } from 'lucide-vue-next';

interface HealthResponse {
    status: 'ok' | 'error';
    time: string;
    services?: {
        app: string;
        db?: string;
    };
    php_version?: string;
    laravel_version?: string;
}

const health = ref<HealthResponse | null>(null);
const loading = ref(true);
const error = ref<string | null>(null);

const fetchHealth = async () => {
    loading.value = true;
    error.value = null;
    try {
        const res = await fetch('/api/health', { headers: { Accept: 'application/json' } });
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        health.value = await res.json();
    } catch (e: any) {
        error.value = e?.message ?? 'unknown error';
    } finally {
        loading.value = false;
    }
};

onMounted(fetchHealth);
</script>

<template>
    <Head title="SageCoders · Test" />

    <div class="min-h-screen bg-gradient-to-br from-slate-950 via-slate-900 to-slate-950 text-slate-100 flex flex-col">
        <!-- Header -->
        <header class="px-6 py-4 border-b border-slate-800/60 flex items-center gap-3">
            <FlaskConical class="w-6 h-6 text-emerald-400" />
            <span class="font-mono text-sm tracking-wider text-slate-400">sagecoders / test</span>
        </header>

        <!-- Main -->
        <main class="flex-1 flex items-center justify-center px-6">
            <div class="max-w-2xl w-full text-center space-y-8">
                <!-- Hero icon -->
                <div class="flex justify-center">
                    <div class="relative">
                        <div class="absolute inset-0 bg-emerald-500/20 blur-3xl rounded-full" />
                        <Rocket class="w-20 h-20 text-emerald-400 relative" :stroke-width="1.5" />
                    </div>
                </div>

                <!-- Title -->
                <div class="space-y-3">
                    <h1 class="text-5xl md:text-6xl font-bold tracking-tight">
                        SageCoders <span class="text-emerald-400">test</span>
                    </h1>
                    <p class="text-slate-400 text-lg">
                        Laravel + Inertia + Vue 3 + TypeScript + Tailwind + Lucide
                    </p>
                </div>

                <!-- Health check card -->
                <div class="bg-slate-900/60 backdrop-blur border border-slate-800 rounded-2xl p-6 text-left space-y-4">
                    <div class="flex items-center justify-between">
                        <span class="font-mono text-xs uppercase tracking-widest text-slate-500">
                            GET /api/health
                        </span>
                        <button
                            @click="fetchHealth"
                            :disabled="loading"
                            class="text-xs px-3 py-1.5 rounded-md border border-slate-700 hover:border-emerald-500 hover:text-emerald-400 transition disabled:opacity-50 flex items-center gap-1.5"
                        >
                            <Loader2 v-if="loading" class="w-3 h-3 animate-spin" />
                            <span>{{ loading ? 'fetching…' : 'recheck ↻' }}</span>
                        </button>
                    </div>

                    <div v-if="error" class="flex items-start gap-2 text-rose-400 text-sm font-mono">
                        <AlertCircle class="w-4 h-4 mt-0.5 shrink-0" />
                        <span>{{ error }}</span>
                    </div>

                    <pre
                        v-else-if="health"
                        class="text-xs font-mono text-slate-300 overflow-x-auto whitespace-pre-wrap break-all"
                    ><span class="text-slate-500">{</span>
  <span class="text-sky-400">"status"</span>: <span class="text-emerald-400">"{{ health.status }}"</span>,
  <span class="text-sky-400">"time"</span>: <span class="text-amber-400">"{{ health.time }}"</span><template v-if="health.services">,
  <span class="text-sky-400">"services"</span>: <span class="text-slate-500">{{ health.services }}</span></template><template v-if="health.php_version">,
  <span class="text-sky-400">"php_version"</span>: <span class="text-amber-400">"{{ health.php_version }}"</span></template><template v-if="health.laravel_version">,
  <span class="text-sky-400">"laravel_version"</span>: <span class="text-amber-400">"{{ health.laravel_version }}"</span></template>
<span class="text-slate-500">}</span></pre>

                    <div v-else class="text-slate-500 text-sm font-mono">awaiting…</div>

                    <div v-if="health?.status === 'ok'" class="flex items-center gap-2 text-emerald-400 text-sm">
                        <CheckCircle2 class="w-4 h-4" />
                        <span>All systems operational</span>
                    </div>
                </div>

                <!-- Stack badges -->
                <div class="flex flex-wrap justify-center gap-2 text-xs">
                    <span class="px-3 py-1 rounded-full bg-slate-800/60 border border-slate-700 text-slate-300">Laravel 13</span>
                    <span class="px-3 py-1 rounded-full bg-slate-800/60 border border-slate-700 text-slate-300">Inertia v2</span>
                    <span class="px-3 py-1 rounded-full bg-slate-800/60 border border-slate-700 text-slate-300">Vue 3</span>
                    <span class="px-3 py-1 rounded-full bg-slate-800/60 border border-slate-700 text-slate-300">TypeScript</span>
                    <span class="px-3 py-1 rounded-full bg-slate-800/60 border border-slate-700 text-slate-300">Tailwind 3</span>
                    <span class="px-3 py-1 rounded-full bg-slate-800/60 border border-slate-700 text-slate-300">Lucide</span>
                    <span class="px-3 py-1 rounded-full bg-slate-800/60 border border-slate-700 text-slate-300">Filament v3</span>
                    <span class="px-3 py-1 rounded-full bg-slate-800/60 border border-slate-700 text-slate-300">MySQL 8</span>
                    <span class="px-3 py-1 rounded-full bg-slate-800/60 border border-slate-700 text-slate-300">Docker</span>
                </div>
            </div>
        </main>

        <!-- Footer -->
        <footer class="px-6 py-4 border-t border-slate-800/60 text-center text-xs text-slate-500 font-mono">
            test.sagecoders.com · Caddy reverse proxy → Docker container :3002
        </footer>
    </div>
</template>
