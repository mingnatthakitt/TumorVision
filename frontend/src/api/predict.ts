// In production, frontend is served by FastAPI on the same origin — use relative URLs
// In dev, VITE_API_URL can point to the local backend (e.g. http://localhost:8000)
const API_BASE = import.meta.env.VITE_API_URL || '';

export interface Prediction {
  label: string;
  confidence: number;
}

export interface PredictionResponse {
  predictions: Prediction[];
  medgemma_verification?: {
    verified_answer: string;
    explanation: string;
  };
  model_type?: string;
}

export async function predictTumor(
  imageFile: File,
  modelType: string = '44BTIS',
  verify: boolean = false
): Promise<PredictionResponse> {
  const formData = new FormData();
  formData.append('file', imageFile);
  formData.append('model_type', modelType);
  formData.append('verify', String(verify));

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

export async function checkHealth(): Promise<{ "44BTIS": boolean, "17ConVext": boolean }> {
  try {
    const res = await fetch(`${API_BASE}/health`, { signal: AbortSignal.timeout(3000) });
    const data = await res.json();
    return {
      "44BTIS": data.models?.["44BTIS"] === true,
      "17ConVext": data.models?.["17ConVext"] === true
    };
  } catch {
    return { "44BTIS": false, "17ConVext": false };
  }
}
