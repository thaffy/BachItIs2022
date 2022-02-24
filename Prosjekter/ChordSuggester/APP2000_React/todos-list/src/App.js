import React from 'react';
import './App.css';

// Application Meta & Content
import {BrowserRouter as Router, Switch, Route} from 'react-router-dom'
import Header from './MyComponents/Header'
import Footer from './MyComponents/Footer'
import About from './MyComponents/About'

// Application Logic
import AddTodo from './MyComponents/AddTodo'
import Todos from './MyComponents/Todos'



function App() {
  return (
    <div className="App">
      <Router>
        <Header title="My Todo-list" searchBar={false}/>

        <Switch>
          <Route exact path ='/' render={() => {
            return(
              <>
              <AddTodo/>
              <Todos/>
              </>
            )
          }}>
          </Route>

          <Route exact path='/about'>
            <About/>
          </Route>
        </Switch>

        <Footer/>
      </Router>
    </div>
  );
}

export default App;
