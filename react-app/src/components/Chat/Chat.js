import React, { useState, useRef, useEffect } from "react";
import { useParams } from "react-router-dom";
import { useSelector, useDispatch } from "react-redux";
import { io } from 'socket.io-client';
import { chatPost, chatForChannel } from "../../store/chats"
import { deleteChat } from "../../store/chats";
import './index.css';

let socket = io(process.env.REACT_APP_BASE_URL || 'http://127.0.0.1:5000/');

const Chat = ({ server }) => {
    const [chatInput, setChatInput] = useState("");
    const user = useSelector(state => state.session.user);
    const dispatch = useDispatch();
    let chats = useSelector(state => state.chats);
    const { channelId } = useParams();

    //Auto scroll feature
    const divRef = useRef(null);

    useEffect(() => {
        divRef.current.scrollIntoView({ behavior: 'smooth' });
    });

    useEffect(() => {
        // render the chat messages on the selected channel
        if (channelId) {
            dispatch(chatForChannel(channelId))
            // attempt to reconnect if disconnected
            if (socket.disconnected) {
                socket = io('http://127.0.0.1:5000/');
            }
            // listen for chat messages from the server
            socket.on("chat", (data) => {
                // render incoming chat message only in the correct channel
                if (data?.chat.channel_id == channelId) {
                    dispatch(chatPost(data))
                }
            })
            // listen for delete chat messages
            socket.on("delete-chat", (data) => {
                // render incoming chat message only in the correct channel
                console.log('data------: ', data)
                if (data?.channel_id == channelId) {
                    // dispatch deleted chat post
                    dispatch(deleteChat(data.chat_id))
                }
            })
        }
        return (() => {
                socket.disconnect()
        })
    }, [channelId])

    const sendChat = async (e) => {
        e.preventDefault()
        socket.emit("chat", { user, chat: chatInput, channel_id: channelId });
        // dispatch(chatPost(channelId, chatInput))
        setChatInput("")
    }

    const handleDeleteChat = (e, { id }) => {
        e.preventDefault();
        socket.emit("delete-chat", { id });
    }

    const ShowChats = () => {
        return chats?.map((chat) => {
            const isSessionUser = chat.owner_id === user.id;
            const date = new Date(chat.created_on);
            const localTime = date.toLocaleString(date)
            const slicedLocalTime = localTime.slice(0, localTime.indexOf(":") + 3) + localTime.slice(localTime.indexOf(":") + 6) // remove the seconds time
            return (
                <div id="previousMessages" key={chat.id}>
                    <div className={isSessionUser ? "chat_user-active" : "Chat_user"}>
                        {chat.user.username}
                        {server.owner_id === chat.user.id && (
                            <small id="admin-small-text">server admin</small>
                        )}
                        <small id="chat-date">{slicedLocalTime}</small>
                        {isSessionUser && (
                            <button id="btn-delete-chat" type="button" onClick={(e) => handleDeleteChat(e, chat)}>delete</button>
                        )}
                    </div>
                    <div id="Chat_message">{chat.content}</div>
                </div>
            );
        })
    }

    return (user && (
        <>
            <div className="show-chats-container">
                <ShowChats />
                <div ref={divRef} />
            </div>
            {channelId && (
                <form id="chat-form" method="POST" onSubmit={sendChat}>
                    <div id="chat-container">
                        <input
                            type="text"
                            placeholder="Message"
                            value={chatInput}
                            onChange={(e) => setChatInput(e.target.value)}
                            required
                            maxLength={500}
                        />
                        <button type="submit">
                            <i className="far fa-paper-plane"></i>
                        </button>
                    </div>
                </form>
            )}
        </>
    )
    )
};


export default Chat;
