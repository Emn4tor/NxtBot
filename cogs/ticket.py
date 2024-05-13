import discord
from discord.ext import commands
from discord.commands import slash_command
from discord.ui import Button, View
class TicketCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    @commands.has_permissions(administrator=True)
    async def setupticket(self, ctx):
        embed = discord.Embed(
            title="Ticket System",
            description="React with 🎫 to open a ticket",
            color=discord.Color.orange()
        )
        embed.set_footer(text="NxtBot Ticket System")
        embed.set_thumbnail(url=ctx.guild.icon.url)
        msg = await ctx.send(embed=embed)
        await msg.add_reaction("🎫")
        await ctx.respond("Ticket System setup successfully", ephemeral=True)

    class TicketView(View):
        def __init__(self, ticket_channel, member):
            super().__init__()
            self.ticket_channel = ticket_channel
            self.member = member

        @discord.ui.button(label='Close Ticket', style=discord.ButtonStyle.danger)
        async def close_ticket(self, button: Button, interaction: discord.Interaction):
            await self.ticket_channel.delete(reason=f"Ticket closed by {interaction.user}")
            await interaction.response.send_message(f"Ticket closed by {interaction.user}", ephemeral=True)

        @discord.ui.button(label='Claim Ticket', style=discord.ButtonStyle.primary)
        async def claim_ticket(self, button: Button, interaction: discord.Interaction):
            # Check if the user has the "ticket" role
            ticket_role = discord.utils.get(interaction.guild.roles, name="ticket")
            if ticket_role in interaction.user.roles:
                await interaction.response.send_message(f"{interaction.user.mention} claimed the ticket",
                                                        ephemeral=False)
                # Disable the button
                button.disabled = True
                # Update the button
                await interaction.message.edit(view=self)
            else:
                await interaction.response.send_message("You don't have the 'ticket' role.", ephemeral=True)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.emoji.name == "🎫":
            guild = self.bot.get_guild(payload.guild_id)
            member = guild.get_member(payload.user_id)

            # Check if the member is a bot
            if member.bot:
                return

            message = await self.bot.get_channel(payload.channel_id).fetch_message(payload.message_id)
            await message.remove_reaction(payload.emoji, member)

            category = discord.utils.get(guild.categories, name="Tickets")
            if category is None:
                category = await guild.create_category("Tickets")
            ticket = await category.create_text_channel(f"ticket-{member.display_name}")
            await ticket.set_permissions(member, read_messages=True, send_messages=True)
            await ticket.set_permissions(guild.default_role, read_messages=False)
            embed = discord.Embed(
                title="Ticket System",
                description="Please wait for a staff member to assist you",
                color=discord.Color.green()
            )
            ticket_role = discord.utils.get(guild.roles, name="ticket")
            embed.set_footer(text="NxtBot Ticket System")

            # Store the messages in variables
            staff_message = await ticket.send(f"Staff: {ticket_role.mention}")
            user_message = await ticket.send(f"User: {member.mention}")

            # Delete the messages
            await staff_message.delete()
            await user_message.delete()

            view = self.TicketView(ticket, member)

            # Send the view with the embed message
            await ticket.send(embed=embed, view=view)
def setup(bot):
    bot.add_cog(TicketCog(bot))