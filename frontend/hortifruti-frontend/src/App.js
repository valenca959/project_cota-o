import { BrowserRouter as Router} from 'react-router-dom';

import Navbar from './components/layout/Navbar';
import Footer from './components/layout/Footer';


function App() {
  return (
    <Router>
      <Navbar />
      <main>
        conteudo
      </main>
      <Footer />
    </Router>
  );
}

export default App;
