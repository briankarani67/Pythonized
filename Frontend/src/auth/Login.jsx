import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
// import { loginUser } from '../../api/authApi';
import './Login.css'; // Create this file in the same folder
// import LoadingOverlay from './LoadingOverlay';

const Login = () => {
    return (
        <div className="login-wrapper">
            {/* {loading && <LoadingOverlay />} */}
            <div className="login-card">
                <div className="login-header">
                    <h2>Welcome Back</h2>
                    <p>Please enter your details to sign in</p>
                </div>

                {/* {error && <div className="error-banner">{error}</div>} */}

                <form  className="login-form">
                    <div className="input-field">
                        <label htmlFor="email">Email Address</label>
                        <input 
                            type="email" 
                            id="email"
                            name="email"
                            placeholder="name@example.com"
                            required 
                            
                        />
                    </div>

                    <div className="input-field">
                        <div className="label-row">
                            <label htmlFor="password">Password</label>
                            {/* <Link to="/forgotpassword" id="forgot-link">Forgot?</Link> */}
                        </div>
                        <input 
                            type="password" 
                            id="password"
                            name="password"
                            placeholder="••••••••"
                            required 
                         
                        />
                    </div>

                    <button type="submit" className="login-button" disabled={loading}>
                        {loading ? 'Signing In...' : 'Sign In'}
                    </button>
                </form>

                <div className="login-footer">
                    <p>Don't have an account? <Link to="/signup">Create account</Link></p>
                </div>
            </div>
        </div>
    );
};

export default Login;