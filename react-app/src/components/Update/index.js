import React, { useEffect, useState } from "react";
import { NavLink, useParams, useHistory } from "react-router-dom";
import { useSelector, useDispatch } from "react-redux";
import { updateServer, getServer } from "../../store/servers"


// PUT - perform an update on a server
function Update() {
   let dispatch = useDispatch()
   let history = useHistory()
   const { id } = useParams();
   const server = useSelector((state) => {
      return state.servers.currentServer;
   });

   const [file, setFile] = useState("");
   const [serverName, setServerName] = useState("");
   const [errors, setErrors] = useState([]);

   const updateServ = (e) => {
      const errors = [];
      const validImageTypes = new Set(["image/png", "image/jpg", "image/jpeg"])

      // only validate file if it exist when updating
      if (file) {
         if (file.size > 2000400) {
            errors.push("File is too large. Please select a file smaller than 2MB.")
         }

         if (!validImageTypes.has(file.type)) {
            errors.push("Please select a file with only .png, .jpeg, or .jpg extensions.");
         }
      }
      e.preventDefault();
      if (errors.length > 0) {
         setErrors(errors);
         return;
      }
      dispatch(updateServer(id, file, serverName))
      history.push(`/servers/${server?.id}`)
   }

   useEffect(() => {
      dispatch(getServer(id))
   }, [dispatch])

   return (
      <div id="delete__container">
         <form onSubmit={updateServ}>
            {errors.length > 0 && (
               errors.map((error, idx) => (
                  <h5 className="errors" key={idx}>
                     {error}
                  </h5>
               ))
            )}
            <h1 id="server__question">Do you want to update server {server?.name}?</h1>

            <label className="form_label">Select File <small><i>Optional</i></small></label>
            <input type="file" name="image_url" className="form-input" onChange={e => setFile(e.target.files[0])} accept=".png, .jpg, .jpeg" />

            <label className="form_label">Server Name</label>
            <input type="text" name="server_name" className="form-input" onChange={e => setServerName(e.target.value)} required maxLength={15} />

            <button type="submit" id="delete" className="delete__buttons">Submit</button>
            <NavLink to={`/servers/${server?.id}`}>
               <button id="cancel" className="delete__buttons">Cancel</button>
            </NavLink>
         </form>
      </div>
   )
}

export default Update;
