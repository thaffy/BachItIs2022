import React from 'react'
import TodoItems from './TodoItems'

const Todos = (props) => {
    let mystyle={
        minHeight:'70vh',
        margin:"40px auto"
    }
  return (
    <div className='container' style={mystyle}>
        <h3>My Todo-list</h3>
        {props.todos.length===0 ? "Todo-list is empty":
            props.todos.map((todo)=>{
                return(
                <>
                    <TodoItems todo={todo} key={todo.sno} onDelete={props.onDelete}/>
                    <br/>
                </>
                )
            })
        }
    </div>
  )
}

export default Todos
