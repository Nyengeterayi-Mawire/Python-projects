const Nav = () => {
    return (
        <nav className="Nav-bar"> 
            <div className="Logo-box">
                <img src="COD-Logo.png" className="Logo" /> 
            </div>
            
            <ul className="Middle">
                <li><a >Games</a></li>
                <li><a href='#slide2'>Seasons</a></li>
                <li><a href='#More'>New</a></li>
                <li><a href='#slide3'>Get</a></li>
            </ul>
            <ul className="Right">
                <li><a>Login</a></li>
                <li><a>Create Account</a></li>
            </ul>
        </nav>
    )
}
export default Nav;