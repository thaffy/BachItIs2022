import React, { useEffect, useState } from 'react';
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
  let initTodo;
  if(localStorage.getItem("todos")===null){
    initTodo=[];
  }
  else{
    initTodo = JSON.parse(localStorage.getItem("todos"));
  }
  const onDelete = (todo) => {
    console.log("Deleting todo..",todo)
    setTodos(todos.filter((e)=>{
      return e!==todo;
    }));
  }
  const addTodo = (title,desc) => {
    let sno;
    if(todos.lenght===0){
      sno=1
    }
    else {
      sno = todos[todos.lenght-1]-sno+1;
    }
    const myTodo= {
      sno: sno,
      title: title,
      desc: desc
    }
    setTodos([...todos, myTodo]);
    console.log(myTodo);
  }
  const[todos,setTodos] = useState(initTodo);
  useEffect(()=> {
    localStorage.setItem("todos", JSON.stringify(todos));},[todos])

  return (
    <div className="App">
      <Router>
        <Header title="My Todo-list" searchBar={false}/>

        <Switch>
          <Route exact path ='/' render={() => {
            return(
              <>
              <AddTodo addTodo={addTodo}/>
              <Todos todos={todos} onDelete={onDelete}/>
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
