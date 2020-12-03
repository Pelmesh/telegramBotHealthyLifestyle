<#import "parts/common.ftlh" as c>
<#import "parts/header.ftlh" as h>

<@c.page>
    <@h.page/>

<#if user??>
    <div class="form-group container col-3 mt-5">
        <ul class="list-group">
            <li class="list-group-item">Name: ${user.name!}</li>
            <li class="list-group-item">Mail: ${user.email!}</li>
            <li class="list-group-item">Gender: ${body.gender!}</li>
            <li class="list-group-item">Age: ${body.age!}</li>
            <li class="list-group-item">AMR: ${body.AMR!}</li>
            <li class="list-group-item">BMR: ${body.BMR!}</li>
            <li class="list-group-item">Purpose: ${body.purpose!}</li>
            <li class="list-group-item">Height: ${body.height}</li>
            <li class="list-group-item">Weight: ${body.weight!}</li>
            <li class="list-group-item">Diet: ${body.typeDiet!}</li>
            <li class="list-group-item">Calories: ${body.calRate!}</li>
        </ul>
    </div>

    <div class="container mt-3">
        <table class="table table-sm mt-3 border">
            <thead>
            <tr>
                <th scope="col">Date</th>
                <th scope="col">Purpose</th>
                <th scope="col">Breakfast</th>
                <th scope="col">Lunch</th>
                <th scope="col">Dinner</th>
            </tr>
            </thead>
            <tbody>
            <#list rations as ration>
                <tr>
                    <th scope="row">${ration.date!}</th>
                    <#if ration.purpose == 0>
                       <td> Lose weight </td>
                    <#elseif ration.purpose == 2>
                        <td> Save weight </td>
                    <#elseif ration.purpose == 1>
                        <td> To gain weight </td>
                    </#if>
                    <td><a href="${ration.breakfast.url!}">${ration.breakfast.id!}</a></td>
                    <td><a href="${ration.lunch.url!}">${ration.lunch.id!}</a></td>
                    <td><a href="${ration.dinner.url!}">${ration.dinner.id!}</a></td>
                </tr>
            </#list>
            </tbody>
        </table>
    </div>
</#if>

</@c.page>