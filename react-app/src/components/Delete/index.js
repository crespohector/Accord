import React, { useEffect } from "react";
import { NavLink, useParams, useHistory } from "react-router-dom";
import { useSelector, useDispatch } from "react-redux";
import { deleteServer, getServer } from "../../store/servers"
import './Delete.css'


function Delete() {

   let dispatch = useDispatch()
   let history = useHistory()
   const { id } = useParams();
   const server = useSelector((state) => {
      return state.servers.currentServer;
   });

   const deleteServ = (e) => {
      e.preventDefault();
      dispatch(deleteServer(id))
      history.push("/")
   }

   useEffect(() => {
      dispatch(getServer(id))
    },[dispatch])

   return(
      <div id="delete__container">
            <form onSubmit={deleteServ}>
               <h1 id="server__question">Do you want to delete server {server?.name}?</h1>
               <button type="submit" id="delete" className="delete__buttons">Delete</button>
               <NavLink to={`/servers/${server?.id}`}>
                  <button id="cancel" className="delete__buttons">Cancel</button>
               </NavLink>
            </form>
      </div>
   )
}

export default Delete;
