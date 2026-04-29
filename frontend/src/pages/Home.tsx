import { Link } from 'react-router-dom';
import { motion } from 'framer-motion';
import { BrainCircuit, ShieldCheck, Zap, Activity, Clock, Users, FlaskConical } from 'lucide-react';

const features = [
  { icon: BrainCircuit, title: 'Advanced ML Algorithms', desc: 'Powered by EfficientNetV2, trained on thousands of MRI scans for precise tumor classification.' },
  { icon: Zap, title: 'Rapid Identification', desc: 'Get results in seconds — upload an MRI scan and receive top-3 predictions instantly.' },
  { icon: ShieldCheck, title: 'User-Friendly Interface', desc: 'Simple drag-and-drop upload with clear, visual results that anyone can understand.' },
];

const whyItems = [
  { icon: FlaskConical, title: 'Cutting-Edge Technology', desc: 'Built on the latest advancements in machine learning and medical imaging.' },
  { icon: Clock, title: 'Time Efficiency', desc: 'Rapid diagnosis allows for quicker treatment initiation, potentially saving crucial time.' },
  { icon: Users, title: 'Support for Professionals', desc: 'Augments the expertise of healthcare providers with an additional layer of diagnostic confidence.' },
  { icon: Activity, title: 'Ongoing R&D', desc: 'Commitment to innovation means constantly improving our models and expanding capabilities.' },
];

export default function Home() {
  return (
    <>
      {/* Hero */}
      <section className="hero">
        <div className="container" style={{ display: 'grid', gridTemplateColumns: '1.2fr 1fr', gap: 48, alignItems: 'center' }}>
          <motion.div
            className="hero-content"
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.7 }}
          >
            <div className="hero-badge">
              <Activity size={14} /> AI-Powered Diagnostics
            </div>
            <h1 className="hero-title">
              Welcome to <span className="accent-text">TumorVision</span>
            </h1>
            <p className="hero-description">
              Pioneering the future of medical diagnostics. Our innovative platform harnesses cutting-edge
              machine learning to support healthcare professionals in brain tumor diagnosis.
            </p>
            <div className="hero-actions">
              <Link to="/predict" className="btn-primary">
                <BrainCircuit size={18} /> Try TumorVision
              </Link>
              <Link to="/info" className="btn-secondary">
                Learn About Tumors
              </Link>
            </div>
          </motion.div>

          <motion.div
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ delay: 0.3, duration: 0.7 }}
            style={{ display: 'flex', justifyContent: 'center' }}
          >
            <img
              src="/TumorVision.png"
              alt="TumorVision"
              style={{ maxWidth: 360, borderRadius: 'var(--radius-xl)', opacity: 0.9 }}
            />
          </motion.div>
        </div>
      </section>

      {/* Features */}
      <section className="section">
        <div className="container">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            style={{ textAlign: 'center', marginBottom: 48 }}
          >
            <h2 className="section-title">Key Features</h2>
            <p className="section-subtitle" style={{ margin: '0 auto' }}>
              What makes TumorVision a powerful diagnostic tool
            </p>
          </motion.div>

          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: 24 }}>
            {features.map((f, i) => (
              <motion.div
                key={f.title}
                className="feature-card"
                initial={{ opacity: 0, y: 30 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ delay: i * 0.1 }}
              >
                <div className="feature-icon"><f.icon size={22} /></div>
                <h3 className="feature-title">{f.title}</h3>
                <p className="feature-description">{f.desc}</p>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* Mission */}
      <section className="section" style={{ background: 'var(--bg-secondary)' }}>
        <div className="container">
          <div className="mission-grid">
            <motion.div
              initial={{ opacity: 0, x: -30 }}
              whileInView={{ opacity: 1, x: 0 }}
              viewport={{ once: true }}
            >
              <h2 className="section-title">
                Our <span className="accent-text">Mission</span>
              </h2>
              <p style={{ color: 'var(--text-secondary)', marginBottom: 32, lineHeight: 1.7 }}>
                TumorVision is more than just an AI tool — it's a lifeline in the fight against
                terminal illnesses. Our mission has two pillars:
              </p>
              <div className="mission-item">
                <div className="mission-item-number">1</div>
                <div className="mission-item-content">
                  <h4>Enhance Patient Outcomes</h4>
                  <p>By providing rapid and accurate diagnoses, we aim to significantly improve
                  the prognosis for individuals facing potential brain tumors.</p>
                </div>
              </div>
              <div className="mission-item">
                <div className="mission-item-number">2</div>
                <div className="mission-item-content">
                  <h4>Empower Healthcare Professionals</h4>
                  <p>We equip medical experts with state-of-the-art technology, allowing them
                  to make informed decisions with unprecedented speed and precision.</p>
                </div>
              </div>
            </motion.div>
            <motion.div
              initial={{ opacity: 0, x: 30 }}
              whileInView={{ opacity: 1, x: 0 }}
              viewport={{ once: true }}
            >
              <img src="/model3d.jpg" alt="3D Brain Model" />
            </motion.div>
          </div>
        </div>
      </section>

      {/* Why Choose */}
      <section className="section">
        <div className="container" style={{ maxWidth: 800, margin: '0 auto' }}>
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
          >
            <h2 className="section-title">
              Why Choose <span className="accent-text">TumorVision?</span>
            </h2>
          </motion.div>
          <div className="why-list">
            {whyItems.map((item, i) => (
              <motion.div
                key={item.title}
                className="why-item"
                initial={{ opacity: 0, x: -20 }}
                whileInView={{ opacity: 1, x: 0 }}
                viewport={{ once: true }}
                transition={{ delay: i * 0.08 }}
              >
                <item.icon size={20} className="why-icon" />
                <div>
                  <h4>{item.title}</h4>
                  <p>{item.desc}</p>
                </div>
              </motion.div>
            ))}
          </div>
        </div>
      </section>
    </>
  );
}
