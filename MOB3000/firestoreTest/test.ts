const Firestore = require('@google-cloud/firestore');
// import * as keyfile from './key/raviolist-1aad5-firebase-adminsdk-sksna-086b183298.json'




const db = new Firestore({
  projectId: 'raviolist-1aad5',
  keyFilename: './key/raviolist-1aad5-firebase-adminsdk-sksna-086b183298.json',
});


const testAddData = async () => {
    const userID = "1A654"
    const listName ="Gotta buy Fruit"
    const docRef = db.collection('testListStructure').doc(userID + listName);


    await docRef.set({
        listID: 1,
        listName : "List 1",
        description : "We need a lot of Stuff here, and bunch of cucumbers also!",
        createdBy : {
            userID : userID,
            userName : "Terje Fjern"
        },
        isActive: true,
        isPublic: false,
        isRepeating: true,
        created : new Date().toDateString(),
        lastUpdated : new Date().toDateString(),
        items: [
            {
                itemID : 1,
                name : "Apple",
                category : {
                    catagoryID : 1,
                    categoryName : "Fruit"
                },
                quantity : 1
            },
            {
                itemID : 2,
                name : "Orange",
                category : {
                    catagoryID : 1,
                    categoryName : "Fruit"
                },
                quantity : 2
            }
        ]
    })
    .then(() => {
        console.log('Document successfully written!');
    })
}


testAddData();