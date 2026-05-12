import { useState } from 'react';
import { motion } from 'framer-motion';
import { Search } from 'lucide-react';
import TumorCard from '../components/TumorCard';

const tumorData = [
  { name: 'Astrocytoma', desc: 'A type of tumor that originates from astrocytes, which are star-shaped glial cells in the brain and spinal cord. Astrocytomas can range from low-grade (slow-growing) to high-grade (fast-growing and malignant).', prefix: 'astrocytoma' },
  { name: 'Carcinoma', desc: 'A type of cancer that originates in the epithelial cells, which line the inside and outside surfaces of the body. Carcinomas can occur in many parts of the body, such as the skin, lungs, breast, and gastrointestinal tract.', prefix: 'carcinoma' },
  { name: 'Ependymoma', desc: 'A tumor that arises from ependymal cells lining the ventricles of the brain and the central canal of the spinal cord. Ependymomas can occur in both children and adults, with varying degrees of aggressiveness.', prefix: 'ependymoma' },
  { name: 'Ganglioglioma', desc: 'A rare type of brain tumor that arises from ganglion cells (a type of neuron) and glial cells. Gangliogliomas are generally slow-growing and considered low-grade.', prefix: 'ganglioglioma' },
  { name: 'Germinoma', desc: 'A type of germ cell tumor that most commonly occurs in the brain, particularly in the pineal and suprasellar regions. Germinomas are usually highly sensitive to radiation therapy and have a good prognosis.', prefix: 'germinoma' },
  { name: 'Glioblastoma', desc: 'The most aggressive type of primary brain tumor, also known as glioblastoma multiforme (GBM). It originates from astrocytes and is characterized by rapid growth and a tendency to spread quickly within the brain.', prefix: 'glioblastoma' },
  { name: 'Granuloma', desc: 'A small area of inflammation caused by the accumulation of immune cells. Granulomas can form in response to infections, inflammation, or foreign substances, and are often found in tuberculosis or sarcoidosis.', prefix: 'granuloma' },
  { name: 'Medulloblastoma', desc: 'A type of malignant brain tumor that primarily affects children and arises in the cerebellum or posterior fossa. Medulloblastomas are fast-growing and can spread to other parts of the brain and spinal cord.', prefix: 'medulloblastoma' },
  { name: 'Meningioma', desc: 'A tumor that arises from the meninges, the membranes that surround the brain and spinal cord. Meningiomas are usually benign and slow-growing, but in some cases, they can be atypical or malignant.', prefix: 'meningioma' },
  { name: 'Neurocytoma', desc: 'A rare, typically benign tumor that arises from neurons, usually in the ventricular system of the brain. Central neurocytomas are the most common subtype and are generally considered low-grade.', prefix: 'neurocytoma' },
  { name: 'Oligodendroglioma', desc: 'A type of glioma that originates from oligodendrocytes, which produce the myelin sheath around nerve fibers. Oligodendrogliomas are usually slow-growing but can become more aggressive over time.', prefix: 'oligodendroglioma' },
  { name: 'Papilloma', desc: 'A benign tumor that arises from epithelial cells and forms a wart-like growth. Papillomas can occur in various parts of the body, including the skin, bladder, and respiratory tract.', prefix: 'papilloma' },
  { name: 'Schwannoma', desc: 'A usually benign tumor that arises from Schwann cells, which form the protective covering around nerve fibers. Schwannomas are most commonly found on the peripheral nerves.', prefix: 'schwannoma' },
  { name: 'Tuberculoma', desc: 'A granulomatous lesion caused by the Mycobacterium tuberculosis infection, most commonly found in the brain or lungs. Tuberculomas can cause symptoms depending on their location.', prefix: 'tuberculoma' },
];

const tumorData17 = [
  { name: 'Glioma', desc: 'A broad category of tumors that occur in the brain and spinal cord, including Astrocytoma, Ganglioglioma, Glioblastoma, Oligodendroglioma, and Ependymoma. The ConVext model groups these for improved generalization.', prefix: 'glioma' },
  { name: 'Meningioma', desc: 'Tumors arising from the membranes surrounding the brain. Includes Low Grade, Atypical, Anaplastic, and Transitional types.', prefix: 'meningioma' },
  { name: 'Neurocytoma', desc: 'Rare tumors typically found in the ventricles of the brain. Includes Central and Extraventricular subtypes.', prefix: 'neurocytoma' },
  { name: 'Other Injuries', desc: 'Non-tumor lesions including Abscesses, Cysts, and various Encephalopathies.', prefix: 'other' },
  { name: 'Schwannoma', desc: 'Usually benign tumors arising from nerve-sheath cells. Includes Acoustic, Vestibular, and Trigeminal types.', prefix: 'schwannoma' },
  { name: 'NORMAL', desc: 'Standard brain tissue with no detectable tumorous or pathological lesions.', prefix: 'normal' },
];

function getImages(prefix: string, is17: boolean): string[] {
  if (is17) {
    return [`/tumorimages/convext/${prefix}.jpg`];
  }
  const exts: Record<string, string[]> = {
    astrocytoma: ['jpg', 'jpg', 'jpg'],
    carcinoma: ['jpg', 'jpg', 'png'],
    ependymoma: ['jpg', 'png', 'jpeg'],
    ganglioglioma: ['jpeg', 'jpg', 'jpg'],
    germinoma: ['jpeg', 'jpeg', 'jpeg'],
    glioblastoma: ['jpeg', 'jpeg', 'jpeg'],
    granuloma: ['jpeg', 'jpg', 'jpg'],
    medulloblastoma: ['jpg', 'jpg', 'jpg'],
    meningioma: ['jpg', 'jpg', 'jpg'],
    neurocytoma: ['jpg', 'jpg', 'jpg'],
    oligodendroglioma: ['jpg', 'jpg', 'jpg'],
    papilloma: ['jpg', 'jpg', 'jpg'],
    schwannoma: ['jpg', 'jpg', 'jpg'],
    tuberculoma: ['jpg', 'jpg', 'jpg'],
  };
  const e = exts[prefix] || ['jpg', 'jpg', 'jpg'];
  return [
    `/tumorimages/path_to_${prefix}_image1.${e[0]}`,
    `/tumorimages/path_to_${prefix}_image2.${e[1]}`,
    `/tumorimages/path_to_${prefix}_image3.${e[2]}`,
  ];
}

export default function TumorInfo() {
  const [search, setSearch] = useState('');
  const [activeTab, setActiveTab] = useState<'44' | '17'>('44');

  const data = activeTab === '44' ? tumorData : tumorData17;

  const filtered = data.filter(t =>
    t.name.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <section className="section">
      <div className="container">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
        >
          <h1 className="section-title">Tumor Type Information</h1>
          <p className="section-subtitle" style={{ marginBottom: 32 }}>
            Knowledge base for the tumor types detected by our models
          </p>
        </motion.div>

        {/* Tabs */}
        <div style={{ 
          display: 'flex', 
          gap: 8, 
          marginBottom: 32, 
          background: 'rgba(255,255,255,0.03)', 
          padding: 4, 
          borderRadius: 'var(--radius-md)',
          width: 'fit-content'
        }}>
          <button 
            onClick={() => setActiveTab('44')}
            style={{
              padding: '8px 16px',
              borderRadius: 'calc(var(--radius-md) - 2px)',
              background: activeTab === '44' ? 'var(--accent-color)' : 'transparent',
              color: activeTab === '44' ? 'white' : 'var(--text-muted)',
              border: 'none',
              fontSize: '0.85rem',
              fontWeight: 600,
              cursor: 'pointer',
              transition: 'all 0.2s'
            }}
          >
            BTIS 44 Classification
          </button>
          <button 
            onClick={() => setActiveTab('17')}
            style={{
              padding: '8px 16px',
              borderRadius: 'calc(var(--radius-md) - 2px)',
              background: activeTab === '17' ? 'var(--accent-color)' : 'transparent',
              color: activeTab === '17' ? 'white' : 'var(--text-muted)',
              border: 'none',
              fontSize: '0.85rem',
              fontWeight: 600,
              cursor: 'pointer',
              transition: 'all 0.2s'
            }}
          >
            ConVext 17 Classification
          </button>
        </div>

        <motion.div
          className="search-bar"
          initial={{ opacity: 0, y: 10 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.1 }}
          style={{ marginBottom: 32 }}
        >
          <Search size={18} className="search-icon" />
          <input
            type="text"
            placeholder={`Search ${activeTab === '44' ? '44-class' : '17-class'} types...`}
            value={search}
            onChange={(e) => setSearch(e.target.value)}
          />
        </motion.div>

        <div className="tumor-grid">
          {filtered.map((tumor, i) => (
            <TumorCard
              key={`${activeTab}-${tumor.name}`}
              name={tumor.name}
              description={tumor.desc}
              images={getImages(tumor.prefix, activeTab === '17')}
              index={i}
            />
          ))}
        </div>

        {filtered.length === 0 && (
          <p style={{ textAlign: 'center', color: 'var(--text-muted)', padding: '60px 0' }}>
            No tumor types match your search.
          </p>
        )}
      </div>
    </section>
  );
}
