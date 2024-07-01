const SHOW_CHAT = "chats/SHOW_CHAT"
const ADD_CHAT = "chats/ADD_CHAT"
const DELETE_CHAT = "chats/DELETE_CHAT";

const showChat = (list) => ({
    type: SHOW_CHAT,
    payload: list
})

const addChat = (content) => ({
    type: ADD_CHAT,
    payload: content
})

const removeChat = (id) => ({
    type: DELETE_CHAT,
    payload: id,
})

//thinking about doing the GET requests in the chat component
export const chatForChannel = (channel_id) => async (dispatch) => {
    const res = await fetch(`/api/chat/${channel_id}`,{
        headers: {
            "Content-Type": "application/json",
        },
    });
    if(res.ok) {
        const data = await res.json();
        dispatch(showChat(data))
    }
}

export const chatPost = (data, id, content) => async (dispatch) => {
    // const res = await fetch(`/api/chat/${id}`, {
    //     method: 'POST',
    //     headers: {
    //         'Content-Type': 'application/json'
    //     },
    //     body: JSON.stringify({
    //         content
    //     })
    // });
    // const data = await res.json();
    // if (data.errors) {
    //     return data;
    // }
    dispatch(addChat(data.chat))
    return {};
}

export const deleteChat = (chatId) => async (dispatch) => {
    // const res = await fetch(`/api/chat/${id}`, {
    //     method: 'DELETE'
    // });
    // const data = await res.json();
    // if (data.errors) {
    //     return data;
    // }
    dispatch(removeChat(chatId))
    return {};
}

export default function chatReducer(state = [], action) {
    let newState;
    switch(action.type) {
        case SHOW_CHAT:
            newState = action.payload.chats;
            return newState;
        case ADD_CHAT:
            newState = [...state, action.payload];
            return newState;
        case DELETE_CHAT:
            // perform a for loop to find the chat instance to delete
            newState = state.filter(obj => {
                return obj.id !== action.payload;
            })
            return newState;

        default:
            return state;
    }

}
