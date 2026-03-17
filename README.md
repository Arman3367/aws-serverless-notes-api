# AWS Serverless Notes API

A simple serverless REST API built on AWS using API Gateway, Lambda, and DynamoDB.

## Overview

This project allows users to create notes, retrieve all notes, and delete notes through HTTP endpoints. It demonstrates a basic serverless architecture without managing any servers.

## Architecture

Client → API Gateway → Lambda → DynamoDB

## AWS Services Used

- API Gateway
- AWS Lambda
- Amazon DynamoDB
- IAM

## Features

- Create a note
- Read all notes
- Delete a note

## API Endpoints

- `POST /notes`
- `GET /notes`
- `DELETE /notes/{id}`

## How It Works

- API Gateway exposes the endpoints
- Lambda runs the Python logic
- DynamoDB stores the notes
- IAM permissions allow Lambda to access DynamoDB

## Sample Request

### Create a note
```json
{
  "content": "my first note"
}
