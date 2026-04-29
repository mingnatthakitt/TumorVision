import { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import UploadArea from '../components/UploadArea';
import PredictionDisplay from '../components/PredictionDisplay';
import { predictTumor, checkHealth, type Prediction } from '../api/predict';

export default function Predict() {
  const [predictions, setPredictions] = useState<Prediction[] | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [backendOnline, setBackendOnline] = useState<boolean | null>(null);

  useEffect(() => {
    checkHealth().then(setBackendOnline);
  }, []);

  const handleFileSelect = async (file: File) => {
    setIsLoading(true);
    setError(null);
    setPredictions(null);

    try {
      const result = await predictTumor(file);
      setPredictions(result.predictions);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Prediction failed');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <section className="section">
      <div className="container" style={{ maxWidth: 800, margin: '0 auto' }}>
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
        >
          <div style={{ display: 'flex', alignItems: 'center', gap: 12, marginBottom: 8 }}>
            <h1 className="section-title" style={{ marginBottom: 0 }}>
              <span className="accent-text">TumorVision</span> — AI Detection
            </h1>
            {backendOnline !== null && (
              <span
                className={`status-dot ${backendOnline ? 'online' : 'offline'}`}
                title={backendOnline ? 'Model loaded' : 'Backend offline'}
              />
            )}
          </div>
          <p className="section-subtitle" style={{ marginBottom: 32 }}>
            Upload a brain MRI scan to identify tumor types using our AI model
          </p>
        </motion.div>

        {/* Steps */}
        <motion.div
          className="steps"
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.1 }}
        >
          <div className="step">
            <div className="step-number">1</div>
            <div className="step-text">
              <strong>Upload</strong>
              Drag & drop or browse for an MRI image
            </div>
          </div>
          <div className="step">
            <div className="step-number">2</div>
            <div className="step-text">
              <strong>Analyze</strong>
              Our AI model processes the scan in seconds
            </div>
          </div>
          <div className="step">
            <div className="step-number">3</div>
            <div className="step-text">
              <strong>Results</strong>
              Get top 3 predictions ranked by probability
            </div>
          </div>
        </motion.div>

        {/* Upload */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.2 }}
          style={{ marginBottom: 32 }}
        >
          <UploadArea onFileSelect={handleFileSelect} isLoading={isLoading} />
        </motion.div>

        {/* Error */}
        {error && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            style={{
              padding: '16px 20px',
              background: 'rgba(239,68,68,0.1)',
              border: '1px solid rgba(239,68,68,0.3)',
              borderRadius: 'var(--radius-md)',
              color: '#f87171',
              marginBottom: 24,
              fontSize: '0.9rem'
            }}
          >
            {error}
          </motion.div>
        )}

        {/* Results */}
        {predictions && <PredictionDisplay predictions={predictions} />}
      </div>
    </section>
  );
}
