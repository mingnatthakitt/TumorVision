import { useState } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { motion, AnimatePresence } from 'framer-motion';

const navItems = [
  { path: '/', label: 'Home' },
  { path: '/predict', label: 'TumorVision' },
  { path: '/info', label: 'Tumor Info' },
];

export default function Navbar() {
  const location = useLocation();
  const [mobileOpen, setMobileOpen] = useState(false);

  return (
    <nav className="navbar">
      <div className="container">
        <Link to="/" className="nav-brand">
          <img src="/TumorVisionLOGO-removebg.png" alt="TumorVision" />
          <span className="nav-brand-text">TumorVision</span>
        </Link>

        <button
          className="nav-mobile-toggle"
          onClick={() => setMobileOpen(!mobileOpen)}
          aria-label="Toggle menu"
        >
          <span /><span /><span />
        </button>

        <ul className={`nav-links ${mobileOpen ? 'open' : ''}`}>
          {navItems.map((item) => (
            <li key={item.path}>
              <Link
                to={item.path}
                className={`nav-link ${location.pathname === item.path ? 'active' : ''}`}
                onClick={() => setMobileOpen(false)}
              >
                {item.label}
                <AnimatePresence>
                  {location.pathname === item.path && (
                    <motion.div
                      className="nav-link-indicator"
                      layoutId="nav-indicator"
                      initial={{ opacity: 0 }}
                      animate={{ opacity: 1 }}
                      exit={{ opacity: 0 }}
                      transition={{ type: 'spring', stiffness: 500, damping: 30 }}
                    />
                  )}
                </AnimatePresence>
              </Link>
            </li>
          ))}
        </ul>
      </div>
    </nav>
  );
}
