# Quickstart: Building the Book

This guide provides instructions on how to set up the development environment and build the Docusaurus-based book locally.

## Prerequisites
- Node.js (v18 or later)
- Yarn

## Installation

Install the project dependencies:

```bash
cd book
yarn
```

## Local Development

To start a local development server:

```bash
cd book
yarn start
```

This command starts a local development server and opens up a browser window at `http://localhost:3000`. Most changes are reflected live without having to restart the server.

## Build

To generate a static build of the website:

```bash
cd book
yarn build
```

This command generates static content into the `build` directory.

## Deployment

The book is set up for deployment to GitHub Pages.

### Using SSH

```bash
cd book
USE_SSH=true yarn deploy
```

### Without SSH

```bash
cd book
GIT_USER=<Your GitHub username> yarn deploy
```

This command builds the website and pushes the `build` directory to the `gh-pages` branch of the repository.
