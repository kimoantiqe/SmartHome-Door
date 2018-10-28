# Material Walkthrough
This is the **STABLE** branch, that uses jQuery as the core. Check the [V2 (under development)](https://github.com/essetwide/material-walkthrough/tree/v2) branch for a Pure ES6 implementation.

A material tour (eg. [Inbox from Google](http://spyrestudios.com/ux-design-from-google-inbox/)) for your site, enhancing the UX.
[See the demo here!](https://essetwide.github.io/material-walkthrough/)

## Features
* Material Design - Have a Material look, based on the tour presented by Google Inbox.
* Customizable - Change the content and colors easily.
* Responsive - Resize the screen and continue enjoying your Walkthrough.
* Simple - With a few lines of code you will got a Walkthrough.
* Compatible - Google Chrome 52.0; Firefox 48.0.2; Microsoft Edge 38.14393.0.0.
* Made with love - Few nights without studying to develop this plugin with much love. 

## Getting Started

### Using through NPM

#### 1. Installing
First, you just need to install the plugin from the NPM Registry.
``` shell
npm install @essetwide/material-walkthrough --save
```

#### 2. Importing
Import the script by your language. Remember that this version of Material Walkthrough depends to have jQuery installed.

##### ES6 `import` Syntax
If your module bundler supports `import` statements.
``` es6
import $ from 'jquery'; // Importing jQuery first
import '@essetwide/material-walkthrough'; // Import the package globaly
import '@essetwide/material-walkthrough/dist/material-walkthrough.css'; // Import the style
```

##### CommonJS `require` Syntax
If your project use `require` pattern.
``` js
var $ = require('jquery'); // Importing jQuery first
require('@essetwide/material-walkthrough'); // Import the package globaly
require('@essetwide/material-walkthrough/dist/material-walkthrough.css'); // Import the style
```

### Using by the ZIP

#### 1. Download and extract the Source
You can download the ZIP from master [here](https://github.com/essetwide/material-walkthrough/archive/master.zip) and extract it in your project.

#### 2. Settup your Code
Load jQuery and include Material-Walkthrough plugin files.
``` html
<head>
        .
        .
        .
        <!-- Material Walkthrough styles -->
        <link rel="stylesheet" href="path/to/material-walkthrough/material-walkthrough.min.css">
</head>
<body>
        .
        .
        .
        <!-- JQuery 3.1 minified -->
        <script src="https://code.jquery.com/jquery-3.1.0.min.js"></script>

        <!-- Material Walkthrough plugin -->
        <script src="path/to/material-walkthrough/material-walkthrough.min.js"></script>
</body>
```

### Using the Plugin

#### 1. Setup your HTML
You don't need any special markup. All you need is add something to identify your HTML element - an `id` or a `class`, by example.
``` html
<a id="step1">Try it Now!</a>
```

#### 2. Call the plugin
Now call the Material Walkthrough initializer function and your walkthrough is ready.
``` js
$.walk([
  {
    target: '#step1', // Your target
    content: 'Here you can begin the walk!', // Hey, it supports HTML codes too!
    color: 'red', // Can be any CSS color, rgb or hex.
    acceptText: 'OK'
  }
]);
```

# License
  Copyright 2018 Esset Software LTD.
 
  Licensed under the Apache License, Version 2.0 (the "License");
  you may not use this files except in compliance with the License.
  You may obtain a copy of the License at
 
  http://www.apache.org/licenses/LICENSE-2.0
 
  Unless required by applicable law or agreed to in writing, software
  distributed under the License is distributed on an "AS IS" BASIS,
  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
  See the License for the specific language governing permissions and
  limitations under the License.
  
# Thanks To
* Thanks to [@galambalazs](https://github.com/galambalazs) for the Lock Scroll code. 
