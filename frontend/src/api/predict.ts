// In production, frontend is served by FastAPI on the same origin — use relative URLs
// In dev, VITE_API_URL can point to the local backend (e.g. http://localhost:8000)
const API_BASE = import.meta.env.VITE_API_URL || '';

export interface Prediction {
  rank: number;
  label: string;
  probability: number;
}

export interface PredictionResponse {
  predictions: Prediction[];
}

export async function predictTumor(file: File): Promise<PredictionResponse> {
  const formData = new FormData();
  formData.append('file', file);

  const response = await fetch(`${API_BASE}/predict`, {
    method: 'POST',
    body: formData,
  });

  if (!response.ok) {
    const error = await response.json().catch(() => ({ detail: 'Prediction failed' }));
    throw new Error(error.detail || `Server error: ${response.status}`);
  }

  return response.json();
}

export async function checkHealth(): Promise<boolean> {
  try {
    const res = await fetch(`${API_BASE}/health`, { signal: AbortSignal.timeout(3000) });
    const data = await res.json();
    return data.model_loaded === true;
  } catch {
    return false;
  }
}
