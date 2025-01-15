import { Link } from 'react-router-dom';
import styles from './Navbar.module.css';
import logo from '../../img/hort_logo.png';

function Navbar() {
    return (
        <nav className={styles.navbar}>
            <Link to="/">
                <img src={logo} alt="hortifrut" />
            </Link>
            <ul className={styles.navLinks}>
                <li><Link to="/">Home</Link></li>
                <li><Link to="/suppliers">Fornecedores</Link></li>
                <li><Link to="/fruits">Frutas</Link></li>
                <li><Link to="/quotes">Preços</Link></li>
            </ul>
        </nav>
    );
}

export default Navbar;