#!/bin/bash

parent_name="melancholia"
module_name="service"


docker run -d --rm \
--name "${parent_name}_${module_name}_1" \
-p 5000:5000 \
"${parent_name}/${module_name}"
