export const catagories : string[] = [
    "Fruits and vegetables",
    "Meats",
    "Dairy",
    "Frozen",
    "Canned Goods",
    "Bread",
    "Baking",
    "Snacks",
    "Drinks",
];


export type Category = {
    catagoryID : number,
    categoryName : string,
}


export type Item = {
    itemID : number,
    name : string,
    category : Category
    quantity : number,
}


export type List = {
    listID : number,
    listName : string,
    createdBy : {
        userID : number,
        userName : string,
    }
    isActive : boolean,
    isRepeating : boolean,
    lastUpdated : Date,
    items : Item[]
}

export type User = {
    userID : number,
    userName : string,
    lastSeen : Date,
    lists : List[]
}


// Eksempel

const user : User = {
    userID : 1,
    userName : "John Doe",
    lastSeen : new Date(),
    lists : [
        {
            listID : 1,
            listName : "Groceries",
            createdBy : {
                userID : 1,
                userName : "John Doe",
            },
            isActive : true,
            isRepeating : true,
            lastUpdated : new Date(),
            items : [
                {
                    itemID : 1,
                    name : "Apple",
                    category : {
                        catagoryID : 1,
                        categoryName : "Fruits and vegetables",
                    },
                    quantity : 2,
                },
                {
                    itemID : 2,
                    name : "Orange",
                    category : {
                        catagoryID : 1,
                        categoryName : "Fruits and vegetables",
                    },
                    quantity : 1,
                },
            ]
        },
    ]
}








