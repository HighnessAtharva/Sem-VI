/* Mixpanel JavaScript SDK begin */
(function(f, b) {
    if (!b.__SV) {
        var e, g, i, h;
        window.mixpanel = b;
        b._i = [];
        b.init = function(e, f, c) {
            function g(a, d) {
                var b = d.split(".");
                2 == b.length && (a = a[b[0]], d = b[1]);
                a[d] = function() {
                    a.push([d].concat(Array.prototype.slice.call(arguments, 0)))
                }
            }
            var a = b;
            "undefined" !== typeof c ? a = b[c] = [] : c = "mixpanel";
            a.people = a.people || [];
            a.toString = function(a) {
                var d = "mixpanel";
                "mixpanel" !== c && (d += "." + c);
                a || (d += " (stub)");
                return d
            };
            a.people.toString = function() {
                return a.toString(1) + ".people (stub)"
            };
            i = "disable time_event track track_pageview track_links track_forms track_with_groups add_group set_group remove_group register register_once alias unregister identify name_tag set_config reset opt_in_tracking opt_out_tracking has_opted_in_tracking has_opted_out_tracking clear_opt_in_out_tracking start_batch_senders people.set people.set_once people.unset people.increment people.append people.union people.track_charge people.clear_charges people.delete_user people.remove".split(" ");
            for (h = 0; h < i.length; h++) g(a, i[h]);
            var j = "set set_once union unset remove delete".split(" ");
            a.get_group = function() {
                function b(c) {
                    d[c] = function() {
                        call2_args = arguments;
                        call2 = [c].concat(Array.prototype.slice.call(call2_args, 0));
                        a.push([e, call2])
                    }
                }
                for (var d = {}, e = ["get_group"].concat(Array.prototype.slice.call(arguments, 0)), c = 0; c < j.length; c++) b(j[c]);
                return d
            };
            b._i.push([e, f, c])
        };
        b.__SV = 1.2;
        e = f.createElement("script");
        e.type = "text/javascript";
        e.async = !0;
        e.src = "undefined" !== typeof MIXPANEL_CUSTOM_LIB_URL ?
            MIXPANEL_CUSTOM_LIB_URL : "file:" === f.location.protocol && "//cdn.mxpnl.com/libs/mixpanel-2-latest.min.js".match(/^\/\//) ? "https://cdn.mxpnl.com/libs/mixpanel-2-latest.min.js" : "//cdn.mxpnl.com/libs/mixpanel-2-latest.min.js";
        g = f.getElementsByTagName("script")[0];
        g.parentNode.insertBefore(e, g)
    }
})(document, window.mixpanel || []);
/* Mixpanel JavaScript SDK end */

/* Mixpanel Wrapper begin */
(function(a,p) {
    
    // If window.mixpanel doesn't exist, return
    if (!a.mixpanel || typeof a.mixpanel.init !== 'function') return;

    // Enumerate available commands
    var commandEnum = [
        'add_group',
        'alias',
        'clear_opt_in_out_tracking',
        'disable',
    /* Ignore getters
        'get_config',
        'get_distinct_id',
        'get_group',
        'get_property',
        'has_opted_in_tracking',
        'has_opted_out_tracking',
    */
    /* Ignore init
        'init'
    */
        'identify',
        'opt_in_tracking',
        'opt_out_tracking',
    /* Ignore push
        'push',
    */
        'register',
        'register_once',
        'remove_group',
        'reset',
        'set_config',
        'set_group',
        'time_event',
        'track',
        'track_forms',
        'track_links',
        'track_with_groups',
        'unregister',
        'people.append',
        'people.clear_charges',
        'people.delete_user',
        'people.increment',
        'people.remove',
        'people.set',
        'people.set_once',
        'people.track_charge',
        'people.union',
        'people.unset',
        'group.remove',
        'group.set',
        'group.set_once',
        'group.union',
        'group.unset'
    ];

    /* The people API can't be used with the .push() interface, so it requires its
     * own helper method. To interact with it, simply use the _mixpanel interface
     * as before.
     *
     * window._mixpanel('<libraryName.>people.set', 'gender', 'm');
     *
     */
    var people = function(mp, cmd, args) {
        // Extract the command
        var peopleCmd = cmd.split('.').pop();

        // Call the respective mixpanel method
        mp.people[peopleCmd].apply(mp.people, args);
    };

    /* To utilize the group API, the command must include the group key and ID as
     * an array in the second argument.
     *
     * window._mixpanel('<libraryName.>.group.set', ['group_key', 'group_id'], {
     *   someGroupProperty: 'someGroupValue'
     * });
     * 
     */
    var group = function(mp, cmd, args) {
        // Extract the command
        var groupCmd = cmd.split('.').pop();

        // Extract the group info
        var groupInfo = args.shift();

        // Validate the group array
        if (!Array.isArray(groupInfo) || groupInfo.length !== 2) return;

        // Get group reference
        var group = mp.get_group.apply(mp, groupInfo);

        // Call the respective group method
        group[groupCmd].apply(group, args);

    };

    // Build the command wrapper logic
    a[p] = a[p] || function() {

        // Build array out of arguments
        var args = [].slice.call(arguments, 0);
        
        // Pick the first argument as the command
        var cmd = args.shift();

        /* Commands can be passed to different namespaces with syntax:
         * window._mixpanel('libraryName.command', arguments)
         */ 
        var libraryName = null;
        var cmdParts = cmd.match(/^([^.]+)\.(.+)$/);
        if (cmdParts && cmdParts.length === 3 && !/people|group/.test(cmdParts[1])) {
            libraryName = cmdParts[1];
            cmd = cmdParts[2];
        } 
        
        // If libraryName is set, use that as the mixpanel interface
        var mp = libraryName ? window.mixpanel[libraryName] : window.mixpanel;

        // Return if namespace not found
        if (!mp) return;

        // If cmd is not one of the available ones, return
        if (commandEnum.indexOf(cmd) === -1) return;

        // Handle people command
        if (/^people\./.test(cmd)) return people(mp, cmd, args);

        // Handle group command
        if (/^group\./.test(cmd)) return group(mp, cmd, args);

        // Push the command to mixpanel
        return mp.push.apply(mp, [[cmd].concat(args)]);

    };
})(window, '_mixpanel')
/* Mixpanel wrapper end */