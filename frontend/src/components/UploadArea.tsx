import { useState, useCallback } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { Upload, X } from 'lucide-react';

interface Props {
  onFileSelect: (file: File) => void;
  isLoading: boolean;
}

export default function UploadArea({ onFileSelect, isLoading }: Props) {
  const [preview, setPreview] = useState<string | null>(null);
  const [dragOver, setDragOver] = useState(false);
  const [fileName, setFileName] = useState('');

  const handleFile = useCallback((file: File) => {
    if (!file.type.startsWith('image/')) return;
    setFileName(file.name);
    const reader = new FileReader();
    reader.onload = (e) => setPreview(e.target?.result as string);
    reader.readAsDataURL(file);
    onFileSelect(file);
  }, [onFileSelect]);

  const handleDrop = useCallback((e: React.DragEvent) => {
    e.preventDefault();
    setDragOver(false);
    const file = e.dataTransfer.files[0];
    if (file) handleFile(file);
  }, [handleFile]);

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) handleFile(file);
  };

  const clearPreview = () => {
    setPreview(null);
    setFileName('');
  };

  return (
    <div>
      <AnimatePresence mode="wait">
        {!preview ? (
          <motion.label
            key="upload"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -20 }}
            className={`upload-zone ${dragOver ? 'drag-over' : ''}`}
            onDragOver={(e) => { e.preventDefault(); setDragOver(true); }}
            onDragLeave={() => setDragOver(false)}
            onDrop={handleDrop}
          >
            <input
              type="file"
              accept="image/jpeg,image/png,image/jpg"
              onChange={handleInputChange}
              style={{ display: 'none' }}
              disabled={isLoading}
            />
            <Upload className="upload-zone-icon" size={48} />
            <p className="upload-zone-title">
              {dragOver ? 'Drop your MRI scan here' : 'Upload an MRI Image'}
            </p>
            <p className="upload-zone-subtitle">
              Drag and drop or click to browse • JPG, PNG
            </p>
          </motion.label>
        ) : (
          <motion.div
            key="preview"
            initial={{ opacity: 0, scale: 0.95 }}
            animate={{ opacity: 1, scale: 1 }}
            exit={{ opacity: 0, scale: 0.95 }}
            className="upload-preview"
          >
            <img src={preview} alt={fileName} />
            {!isLoading && (
              <div className="upload-preview-overlay">
                <button className="upload-btn-remove" onClick={clearPreview} title="Remove">
                  <X size={18} />
                </button>
              </div>
            )}
            {isLoading && (
              <div style={{
                position: 'absolute', inset: 0,
                background: 'rgba(10,14,23,0.7)',
                display: 'flex', alignItems: 'center', justifyContent: 'center'
              }}>
                <div className="spinner">
                  <div className="spinner-ring" />
                  <p className="spinner-text">Analyzing MRI scan...</p>
                </div>
              </div>
            )}
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}
