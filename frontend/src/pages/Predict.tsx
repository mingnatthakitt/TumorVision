import { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import UploadArea from '../components/UploadArea';
import PredictionDisplay from '../components/PredictionDisplay';
import { predictTumor, checkHealth, type Prediction } from '../api/predict';

export default function Predict() {
  const [predictions, setPredictions] = useState<Prediction[] | null>(null);
  const [verification, setVerification] = useState<{ verified_answer: string, explanation: string } | null>(null);
  const [modelType, setModelType] = useState<string>('44BTIS');
  const [isLoading, setIsLoading] = useState(false);
  const [isVerifying, setIsVerifying] = useState(false);
  const [lastFile, setLastFile] = useState<File | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [backendStatus, setBackendStatus] = useState<{ "44BTIS": boolean, "17ConVext": boolean } | null>(null);

  useEffect(() => {
    checkHealth().then(setBackendStatus);
  }, []);

  const handleFileSelect = async (file: File) => {
    setIsLoading(true);
    setError(null);
    setPredictions(null);
    setVerification(null);
    setLastFile(file);

    try {
      const result = await predictTumor(file, modelType, false);
      setPredictions(result.predictions);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Prediction failed');
    } finally {
      setIsLoading(false);
    }
  };

  const handleVerify = async () => {
    if (!lastFile) return;
    setIsVerifying(true);
    setError(null);
    try {
      const result = await predictTumor(lastFile, modelType, true);
      if (result.medgemma_verification) {
        setVerification(result.medgemma_verification);
      }
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Verification failed');
    } finally {
      setIsVerifying(false);
    }
  };

  const models = [
    {
      id: '17ConVext',
      name: '17-Class ConVext',
      pros: 'Better generalization, higher stability',
      cons: 'Grouped classes (less granular)'
    },
    {
      id: '44BTIS',
      name: '44-Class BTIS',
      pros: 'Specific diagnostic mapping (44 types)',
      cons: 'Prone to false positives in edge cases'
    }
  ];

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
            {backendStatus && (
              <span
                className={`status-dot ${backendStatus[modelType as keyof typeof backendStatus] ? 'online' : 'offline'}`}
                title={backendStatus[modelType as keyof typeof backendStatus] ? 'Model loaded' : 'Backend offline'}
              />
            )}
          </div>
          <p className="section-subtitle" style={{ marginBottom: 24 }}>
            Upload a brain MRI scan to identify tumor types using our AI model
          </p>
        </motion.div>

        {/* Model Selection */}
        <motion.div
          className="model-selector"
          initial={{ opacity: 0, y: 10 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.1 }}
          style={{
            display: 'grid',
            gridTemplateColumns: '1fr 1fr',
            gap: '12px',
            marginBottom: '32px'
          }}
        >
          {models.map((m) => (
            <div
              key={m.id}
              onClick={() => setModelType(m.id)}
              style={{
                padding: '16px',
                borderRadius: 'var(--radius-md)',
                background: modelType === m.id ? 'rgba(255,255,255,0.08)' : 'rgba(255,255,255,0.03)',
                border: `1px solid ${modelType === m.id ? 'var(--accent-color)' : 'rgba(255,255,255,0.1)'}`,
                cursor: 'pointer',
                transition: 'all 0.2s ease',
                position: 'relative'
              }}
            >
              <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: 8 }}>
                <span style={{ fontWeight: 600, fontSize: '0.9rem' }}>{m.name}</span>
                {modelType === m.id && <span style={{ color: 'var(--accent-color)', fontSize: '0.8rem' }}>● Active</span>}
              </div>
              <div style={{ fontSize: '0.75rem', color: '#10b981', marginBottom: 2 }}>✓ {m.pros}</div>
              <div style={{ fontSize: '0.75rem', color: '#f87171' }}>✗ {m.cons}</div>
            </div>
          ))}
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
        {predictions && (
          <PredictionDisplay
            predictions={predictions}
            verification={verification || undefined}
            isLoadingVerification={isVerifying}
            onVerify={handleVerify}
            model_used={models.find(m => m.id === modelType)?.name}
          />
        )}
      </div>
    </section>
  );
}
