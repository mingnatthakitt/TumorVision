import { motion } from 'framer-motion';
import type { Prediction } from '../api/predict';

interface Props {
  predictions: Prediction[];
}

export default function PredictionDisplay({ predictions }: Props) {
  return (
    <motion.div
      className="prediction-card"
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
    >
      <h3 style={{ marginBottom: 8, fontSize: '1.1rem', fontWeight: 700 }}>
        Detection Results
      </h3>
      <p style={{ color: 'var(--text-muted)', fontSize: '0.85rem', marginBottom: 16 }}>
        Top 3 predictions ranked by probability
      </p>

      {predictions.map((pred, i) => {
        const rankClass = `rank-${pred.rank}` as const;
        return (
          <motion.div
            key={pred.label}
            className="prediction-rank"
            initial={{ opacity: 0, x: -20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ delay: i * 0.15, duration: 0.4 }}
          >
            <div className={`prediction-rank-badge ${rankClass}`}>
              #{pred.rank}
            </div>
            <div className="prediction-info">
              <p className="prediction-label">{pred.label}</p>
              <div className="prediction-bar-track">
                <motion.div
                  className={`prediction-bar-fill ${rankClass}`}
                  initial={{ width: 0 }}
                  animate={{ width: `${pred.probability}%` }}
                  transition={{ delay: i * 0.15 + 0.2, duration: 0.8, ease: [0.16, 1, 0.3, 1] }}
                />
              </div>
            </div>
            <span className={`prediction-probability ${rankClass}`}>
              {pred.probability.toFixed(1)}%
            </span>
          </motion.div>
        );
      })}
    </motion.div>
  );
}
