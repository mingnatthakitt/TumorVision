import { motion } from 'framer-motion';
import type { Prediction } from '../api/predict';

interface Props {
  predictions: Prediction[];
  verification?: {
    verified_answer: string;
    explanation: string;
  };
  isLoadingVerification?: boolean;
  onVerify?: () => void;
  model_used?: string;
}

export default function PredictionDisplay({ 
  predictions, 
  verification, 
  isLoadingVerification, 
  onVerify, 
  model_used 
}: Props) {
  return (
    <motion.div
      className="prediction-card"
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
    >
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: 8 }}>
        <div>
          <h3 style={{ fontSize: '1.1rem', fontWeight: 700 }}>Detection Results</h3>
          <p style={{ color: 'var(--text-muted)', fontSize: '0.85rem' }}>
            Top 3 predictions from {model_used || 'system'}
          </p>
        </div>
      </div>

      <div style={{ marginBottom: 24 }}>
        {predictions.map((pred, i) => {
          const rank = i + 1;
          const rankClass = `rank-${rank}` as const;
          return (
            <motion.div
              key={pred.label}
              className="prediction-rank"
              initial={{ opacity: 0, x: -20 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ delay: i * 0.15, duration: 0.4 }}
            >
              <div className={`prediction-rank-badge ${rankClass}`}>
                #{rank}
              </div>
              <div className="prediction-info">
                <p className="prediction-label">{pred.label}</p>
                <div className="prediction-bar-track">
                  <motion.div
                    className={`prediction-bar-fill ${rankClass}`}
                    initial={{ width: 0 }}
                    animate={{ width: `${pred.confidence}%` }}
                    transition={{ delay: i * 0.15 + 0.2, duration: 0.8, ease: [0.16, 1, 0.3, 1] }}
                  />
                </div>
              </div>
              <span className={`prediction-probability ${rankClass}`}>
                {pred.confidence.toFixed(1)}%
              </span>
            </motion.div>
          );
        })}
      </div>

      {!verification && !isLoadingVerification && onVerify && (
        <motion.button
          whileHover={{ scale: 1.02 }}
          whileTap={{ scale: 0.98 }}
          onClick={onVerify}
          className="w-full py-3 px-4 rounded-lg bg-gradient-to-r from-blue-600 to-indigo-600 text-white font-semibold shadow-lg flex items-center justify-center gap-2"
        >
          <span>🔬</span>
          Request MedGemma AI Verification
        </motion.button>
      )}

      {(verification || isLoadingVerification) && (
        <motion.div
          initial={{ opacity: 0, height: 0 }}
          animate={{ opacity: 1, height: 'auto' }}
          transition={{ delay: 0.2 }}
          style={{
            marginTop: 16,
            paddingTop: 24,
            borderTop: '1px solid rgba(255,255,255,0.1)'
          }}
        >
          <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 12 }}>
            <div style={{ 
              background: 'linear-gradient(135deg, #FFD700, #FFA500)', 
              width: 24, 
              height: 24, 
              borderRadius: '50%', 
              display: 'flex', 
              alignItems: 'center', 
              justifyContent: 'center',
              fontSize: '0.7rem'
            }}>
              💎
            </div>
            <h4 style={{ fontSize: '0.95rem', fontWeight: 600, color: '#FFD700' }}>
              MedGemma 1.5 4B Verification
            </h4>
          </div>
          <div style={{ 
            background: 'rgba(255,255,255,0.03)', 
            padding: '16px', 
            borderRadius: 'var(--radius-md)',
            border: '1px solid rgba(255,215,0,0.1)'
          }}>
            {isLoadingVerification ? (
              <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
                <div style={{ height: 12, width: '90%', background: 'rgba(255,255,255,0.1)', borderRadius: 4 }} className="animate-pulse" />
                <div style={{ height: 12, width: '100%', background: 'rgba(255,255,255,0.1)', borderRadius: 4 }} className="animate-pulse" />
                <div style={{ height: 12, width: '80%', background: 'rgba(255,255,255,0.1)', borderRadius: 4 }} className="animate-pulse" />
              </div>
            ) : (
              <>
                <p style={{ 
                  color: '#FFD700', 
                  fontSize: '1rem', 
                  fontWeight: 700,
                  marginBottom: 8
                }}>
                  {verification?.verified_answer}
                </p>
                <p style={{ 
                  color: 'rgba(255,255,255,0.9)', 
                  fontSize: '0.85rem', 
                  lineHeight: 1.6,
                  fontStyle: 'italic'
                }}>
                  {verification?.explanation}
                </p>
              </>
            )}
          </div>
        </motion.div>
      )}
    </motion.div>
  );
}
