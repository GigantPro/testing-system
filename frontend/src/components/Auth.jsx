import logo from './assets/logo.png';
import './styles/Auth.scss';

const Reg = () => {
  return (
    <div className='Reg'>
      <div className='header'>
        <img src={logo} alt='stepi' />
      </div>
      <div className='main_content'>
        <p>Вход:</p>
        <form action='' className='auth_form'>
          <input type='text' name='login' itemID='login' className='auth-input' />
          <input type='password' name='login' itemID='login' className='auth-input' />
          <button>Accept</button>
        </form>
      </div>
    </div>
  );
};

export default Reg;
