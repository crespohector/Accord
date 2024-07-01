// convert base64 string to a temp object URL to display image
const convertBase64 = (base64) => {
    // decode base64 string into a string of binary data
    try {
        const binaryImageData = atob(base64);

        /*
        byteCharacters.length gives the length of the byteCharacters string, which represents the number of characters in the decoded base64 data.
        new Array(byteCharacters.length) creates a new array with a length equal to the number of characters in byteCharacters. This array will store the character codes.

        for (let i = 0; i < byteCharacters.length; i++) { ... }: This is a typical for loop that iterates over each character in the byteCharacters string.
        byteCharacters.charCodeAt(i): This method charCodeAt(i) retrieves the Unicode code of the character at position i in the string byteCharacters.
        byteNumbers[i] = byteCharacters.charCodeAt(i);: This assigns the Unicode code of each character in byteCharacters to the corresponding index i in the byteNumbers array.

        In this line of code, byteNumbers is an array containing Unicode code points (or byte values) obtained from a base64-decoded string. Here's what new Uint8Array(byteNumbers) does:
        It's commonly used to manipulate binary data, such as converting byte data into a format that can be used with other APIs, like creating Blobs or manipulating image data.
        */

        const byteNums = new Array(binaryImageData.length);
        for (let i = 0; i < binaryImageData.length; i++) {
            // map every char in the decoded base64 string to a unicode.
            byteNums[i] = binaryImageData.charCodeAt(i);
        }

        // byteNums will be an array of unicode values.
        const byteArray = new Uint8Array(byteNums);
        // Convert binary data to URL
        const blob = new Blob([byteArray], {
            type: 'image/jpeg'
        });
        // create temp image url
        const imageURL = URL.createObjectURL(blob);
        return imageURL;
    }
    catch(err) {
        console.log(err)
        // fallback to a default image
    }
}

export default convertBase64;
