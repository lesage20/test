<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use Illuminate\Http\JsonResponse;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Redis;

class HealthController extends Controller
{
    public function __invoke(): JsonResponse
    {
        $services = [
            'app' => 'ok',
        ];

        // Try DB check
        try {
            DB::connection()->getPdo();
            $services['db'] = 'ok';
        } catch (\Throwable $e) {
            $services['db'] = 'down: ' . substr($e->getMessage(), 0, 80);
        }

        $allOk = ! in_array(false, array_map(
            fn ($s) => str_starts_with($s, 'ok'),
            $services
        ), true);

        return response()->json([
            'status' => $allOk ? 'ok' : 'error',
            'time' => now()->toIso8601String(),
            'services' => $services,
            'php_version' => PHP_VERSION,
            'laravel_version' => app()->version(),
        ], $allOk ? 200 : 503);
    }
}
