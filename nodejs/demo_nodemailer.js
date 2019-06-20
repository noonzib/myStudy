var nodemailer = require('nodemailer');

var transporter = nodemailer.createTransport({
  service: 'gmail',
  auth: {
    user: 'noonzib14@gmail.com',
    pass: '*******'
  }
});

var mailOptions = {
  from: 'noonzib14@gmail.com',
  to: 'sdhsroot@gmail.com, noonzib14@gmail.com',
  subject: 'Sending Email using Node.js',
  text: 'That was easy!'
  html: '<h1>Hello</h1>'
};

transporter.sendMail(mailOptions, function(error, info){
  if (error) {
    console.log(error);
  } else {
    console.log('Email sent: ' + info.response);
  }
});