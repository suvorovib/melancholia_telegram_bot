#!/bin/bash

parent_name="melancholia"
module_name="service"

docker build -t "${parent_name}/${module_name}" .