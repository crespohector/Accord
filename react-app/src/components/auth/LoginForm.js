import React, { useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { Redirect, NavLink } from "react-router-dom";
import { login } from "../../store/session";

import './LoginForm.css'

const LoginForm = () => {
  const [errors, setErrors] = useState([]);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const user = useSelector(state => state.session.user);
  const dispatch = useDispatch();

  const onLogin = async (e) => {
    e.preventDefault();
    const data = await dispatch(login(email, password));
    if (data.errors) {
      const arr = [];
      data.errors.forEach(error => {
        // "Email : email is invalid" => slice the error string after the ":"
        const startIdx = error.indexOf(":") + 2;
        arr.push(error.slice(startIdx));
      })
      setErrors(arr)
    }
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  const demoLogin = async (e, demoUser1 = true) => {
    const email = demoUser1 ? 'demo@aa.io' : "jane@yahoo.com";
    const password = 'password';
    e.preventDefault();
    setErrors([]);
    const data = await dispatch(login(email, password));
    if (data.errors) {
      setErrors(data.errors);
    }
  }
  if (user) {
    return <Redirect to="/" />;
  }

  return (
    <div id="login__background">
      <div id="login__container">
        <h1 id="login__title">Welcome back!</h1>
        <h3 id="login__title--subtitle">We're so excited to see you again!</h3>
        <form onSubmit={onLogin} id="login__form">
          {errors.map((error, idx) => (
            <h5 className="errors" key={idx}>{error}</h5>
          ))}
          <div>
            <label htmlFor="email">Email</label>
            <input
              name="email"
              type="text"
              value={email}
              onChange={updateEmail}
              required
            />
          </div>
          <div>
            <label htmlFor="password" id="password--margin">Password</label>
            <input
              name="password"
              type="password"
              value={password}
              onChange={updatePassword}
              required
            />
          </div>
          <button type="submit" className="button">Login</button>
          <div className="demo-btn-container">
            <button type="submit" className="button" onClick={demoLogin}>Login as Demo User</button>
            <button type="submit" className="button" onClick={(e) => demoLogin(e, false)}>Login as Jane Ford</button>
          </div>
          <div id="register__link">
            <p>Need an account?</p>
            <NavLink to="/sign-up">Register</NavLink>
          </div>
        </form>
      </div>
    </div>
  );
};

export default LoginForm;
