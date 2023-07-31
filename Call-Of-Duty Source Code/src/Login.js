const Login = () => {
    return (
        <div className="Login">
            <h1>Welcome back. Your team AWAITS.</h1> 
            <div className="Login-box">
                <img src="1.jpg" /> 
                <div className="Login-text-box">
                    <h2>LOGIN</h2>               
                    <input placeholder="Username" class="input" name="text" type="text"/>
                    <input placeholder="Password" class="input" name="text" type="text" />
                    <button>
                        <span class="box">
                            LOGIN
                        </span>
                    </button>
                </div>
                

            </div>
        </div>
    )
} 
export default Login;