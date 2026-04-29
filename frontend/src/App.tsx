import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './pages/Home';
import Predict from './pages/Predict';
import TumorInfo from './pages/TumorInfo';

function App() {
  return (
    <BrowserRouter>
      <Navbar />
      <main className="page">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/predict" element={<Predict />} />
          <Route path="/info" element={<TumorInfo />} />
        </Routes>
      </main>
      <footer className="footer">
        <div className="container">
          <p>© 2024 TumorVision — Pioneering AI-Powered Brain Tumor Diagnostics</p>
        </div>
      </footer>
    </BrowserRouter>
  );
}

export default App;
