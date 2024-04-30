
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');
const UserModel=require("./userModel")
// User registration
 async function signup(req, res)  {
try {
const { email, password, phoneNo , name } = req.body;
const hashedPassword = await bcrypt.hash(password, 10);
UserModel.createUser(email,hashedPassword,phoneNo,name ,(err, email) => {
    if (err) {
        console.error('Error creating user:', err);
    } else {
        console.log('User created with email:', email);
    }
});

res.status(201).json({ message: 'User registered successfully' });
} catch (error) {
res.status(500).json({ error: 'Registration failed' });
}
}

// User login
const login= async (req, res) => {
try {
    
const { email, password } = req.body;
UserModel.findByEmail(email, (err, user) => {
    if (err) {
        console.error('Error finding user:', err);
    } else {
        console.log('Found user:', user);
        bcrypt.compare(password, user.password).then((match) => {
const token = jwt.sign({ email:user.email }, 'your-secret-key', {
expiresIn: '1h',
        });
        res.status(200).json({ token });


}

        ).catch((err)=>{
            console.log(err);
return res.status(401).json({ error: 'Authentication  failed 2' });
        })

    }
});
// if (foundUser=={}) {
// return res.status(401).json({ error: 'Authentication failed 1' });
// }
// const passwordMatch = await bcrypt.compare(password, user.password);

// if (!passwordMatch) {
// return res.status(401).json({ error: 'Authentication  failed 2' });
// }
// const token = jwt.sign({ email:user.email }, 'your-secret-key', {
// expiresIn: '1h',
// });
// res.status(200).json({ token });
} catch (error) {
res.status(500).json({ error: 'Login failed' });
}
};

module.exports = {signup, login};