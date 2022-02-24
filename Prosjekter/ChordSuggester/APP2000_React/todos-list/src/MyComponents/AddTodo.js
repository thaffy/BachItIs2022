import React, { useState } from 'react'

const AddTodo = ({addTodo}) => {
    const[title, setTitle] = useState("");
    const[desc, setDesc] = useState("");
    const submit = (e) => {
        e.preventDefault();
        if(!title || !desc) {
            alert("Title or description cannot be blank")
        }
        else{
            addTodo(title,desc);
            setTitle("");
            setDesc("");
        }
    }
  return (
    <div className='container my-3'>
        <h2>Add item to your Todo-list</h2>
        <form onSubmit={submit}>
        <div class="mb-3">
            <label htmlFor="title" class="form-label">Title</label>
            <input type="text" value={title} onChange={(e)=> setTitle(e.target.value)} class="form-control" id="title" aria-describedby="emailHelp"/>
        </div>
        <div class="mb-3">
            <label htmlFor="desc" class="form-label">Description</label>
            <input type="text" value={desc} onChange={(e)=> setDesc(e.target.value)} class="form-control" id="desc"/>
        </div>
        <button type="submit" class="btn btn-primary">Add Todo</button>
        </form>
    </div>
  )
}

export default AddTodo
